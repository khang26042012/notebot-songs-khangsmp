import os
import sys
import argparse
import mido
import pynbs

def midi_to_nbs(midi_path, nbs_path, song_name="NoteBot Song", target_tps=20, vulcan_safe=True):
    mid = mido.MidiFile(midi_path)
    
    notes = []
    current_time_sec = 0.0
    
    for msg in mid:
        current_time_sec += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            pitch = msg.note
            channel = getattr(msg, 'channel', 0)
            velocity = int((msg.velocity / 127.0) * 100)
            
            # Map time to ticks
            tick = int(round(current_time_sec * target_tps))
            
            # Percussion channel
            if channel == 9:
                if pitch in [35, 36]:
                    instrument = 4 # Bass Drum
                    key = 36
                elif pitch in [38, 40]:
                    instrument = 2 # Snare
                    key = 45
                elif pitch in [42, 44, 46]:
                    instrument = 3 # Click / Hat
                    key = 45
                else:
                    instrument = 2
                    key = 45
            else:
                # Melodic notes: Clamp into Note Block 2-octave range (33 to 57)
                clamped_pitch = pitch
                while clamped_pitch < 54:
                    clamped_pitch += 12
                while clamped_pitch > 78:
                    clamped_pitch -= 12
                
                key = clamped_pitch - 21
                
                # Assign instrument
                if pitch < 50:
                    instrument = 1 # Double Bass
                elif pitch > 78:
                    instrument = 6 # Bell
                else:
                    instrument = 0 # Harp / Piano
                    
            notes.append((tick, instrument, key, velocity))
            
    notes.sort(key=lambda x: x[0])
    
    # Filter for Vulcan Anti-Cheat Safe Mode:
    # Max 3 notes per tick to prevent FastClick / InteractSpam detection
    if vulcan_safe:
        filtered_notes = []
        tick_counts = {}
        for t, inst, k, v in notes:
            cnt = tick_counts.get(t, 0)
            if cnt < 3: # Max 3 concurrent notes
                filtered_notes.append((t, inst, k, v))
                tick_counts[t] = cnt + 1
        notes = filtered_notes

    nbs_file = pynbs.new_file(
        song_name=song_name,
        song_author="Meteor NoteBot KhangSMP",
        description="Converted for Meteor Client NoteBot (Vulcan Safe)" if vulcan_safe else "Raw Audio/MIDI NoteBot",
        tempo=target_tps
    )
    
    layers_used = {}
    for tick, inst, key, vel in notes:
        layer = layers_used.get(tick, 0)
        layers_used[tick] = layer + 1
        nbs_file.notes.append(pynbs.Note(
            tick=tick,
            layer=layer,
            instrument=inst,
            key=key,
            velocity=vel
        ))
        
    os.makedirs(os.path.dirname(os.path.abspath(nbs_path)), exist_ok=True)
    nbs_file.save(nbs_path)
    print(f"Successfully converted to {nbs_path} ({len(nbs_file.notes)} notes)!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert MIDI to NBS for Meteor NoteBot")
    parser.add_argument("input_midi", help="Path to input .mid file")
    parser.add_argument("output_nbs", help="Path to output .nbs file")
    parser.add_argument("--name", default="NoteBot Song", help="Song title")
    parser.add_argument("--tps", type=int, default=20, help="Target ticks per second")
    parser.add_argument("--vulcan-safe", action="store_true", default=True, help="Limit max 3 notes per tick")
    
    args = parser.parse_args()
    midi_to_nbs(args.input_midi, args.output_nbs, args.name, args.tps, args.vulcan_safe)
