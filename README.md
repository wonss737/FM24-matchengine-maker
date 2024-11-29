# fm24-matchengine-maker

# Instructions
1. Download below files:

    + main.exe,
    + physical_constraints.jsb,
    + physical_constraints.json.

    Do not delete or move any files; keep them as they are. All files must remain in the same folder.

2. Edit the values in physical_constraints.json. Only modify the values.

    (Do not add new entries, as they will not have any effect.)

    (For detailed descriptions of the values, refer to: FMKorea link.)

3. After editing physical_constraints.json, run main.exe.

    When you run main.exe, the program will output details about the changes and generate a new file: physical_constraints_update.jsb.

4. Move the newly generated physical_constraints_update.jsb into the physics folder located inside the simatch folder.

    Rename the moved file from physical_constraints_update.jsb to physical_constraints.jsb.

    (Overwrite or delete the original physical_constraints.jsb.)

5. Launch "Football Manager 2024 Resource Archiver" from Steam.

    (If it is not installed, go to Steam's "Tools" section and install it.)

6. Create Archive in the Resource Archiver.

    Choose the simatch folder where you placed the new physical_constraints_update.jsb.

7. Move the generated simatch.fmf to the FM24 installation folder.

You can see instruction example at src/usage_example.mp4


# Is it really works?
Yes, it works. Let me explain how it works.

When simatch.fmf is extracted using the FM Resource Archiver, you will find several files.

I specifically modify physical_constraints.jsb within the physics folder.

Opening this file reveals numerous values.

![physical_constraints](https://github.com/wonss737/fm24-matchengine-maker/blob/main/src/physical_constraints.png)

The acceleration_scaler value might look like 10 27 00 00, which, when read in reverse hexadecimal, becomes x00002710 or 10000 in decimal.

I have mapped the positions of all values within physical_constraints.jsb.

Note: Some values like min_delay_for_shirt_tug_do are limited to 2-byte hex values, hence the range of 0–255.

This tool only edits existing values in physical_constraints_update.jsb. 

Adding new entries will not have any effect. 

For example, adding "lob_pass_success_rate": 100 to the JSON file will not change anything in the match engine.

![change_example1](https://github.com/wonss737/fm24-matchengine-maker/blob/main/src/change_example1.gif)

![change_example2](https://github.com/wonss737/fm24-matchengine-maker/blob/main/src/change_example2.gif)

# Modifiable Values and Default Settings
This tool only allows you to edit certain predefined values. Adding new entries to the JSON file will not affect the match engine.

Note: The value min_delay_for_shirt_tug_do is restricted to a range of 0–255.

| Delay | Defaults |
|  ------- |  ------- |
| min_delay_for_ball_lunge_do | 1500 |
| min_delay_for_ball_lunge_receive | 750 |
| min_delay_for_block_tackle_do | 500 |
| min_delay_for_block_tackle_receive | 750 |
| min_delay_for_celebrating_a_goal | 3000 |
| min_delay_for_deflect_ball_do | 250 |
| min_delay_for_deflect_ball_receive | 500 |
| min_delay_for_diving_header | 2000 |
| min_delay_for_foot_up_in_tackle_do | 1000 |
| min_delay_for_foot_up_in_tackle_receive | 3000 |
| min_delay_for_force_opponent_to_lose_ball_do | 500 |
| min_delay_for_force_opponent_to_lose_ball_receive | 500 |
| min_delay_for_getting_injured | 2000 |
| min_delay_for_normal_header | 1000 |
| min_delay_for_obstruct_do | 1000 |
| min_delay_for_obstruct_receive | 2000 |
| min_delay_for_player_stop_to_avoid_collision | 500 |
| min_delay_for_push_opponen_receive | 2000 |
| min_delay_for_push_opponent_do | 500 |
| min_delay_for_shirt_tug_do | 130 |
| min_delay_for_shirt_tug_receive | 500 |
| min_delay_for_shoulder_charge_do | 500 |
| min_delay_for_shoulder_charge_receive | 2000 |
| min_delay_for_slide_tackle_do | 1500 |
| min_delay_for_slide_tackle_receive | 750 |
| min_delay_for_trip_do | 750 |
| min_delay_for_trip_receive | 3000 |
| min_delay_for_two_footed_tackle_do | 1500 |
| min_delay_for_two_footed_tackle_receive | 3000 |
| min_delay_for_violent_act_do | 500 |
| min_delay_for_violent_act_receive | 1000 |
| min_delay_keeper_drop_ball_for_distribution | 1000 |
| min_delay_keeper_save_dive_and_hold_ball | 2000 |
| min_delay_keeper_save_dive_but_not_held | 750 |
| min_delay_keeper_save_intentionally_drop_ball | 500 |
| min_delay_keeper_save_no_dive_hold_ball | 500 |
| min_delay_keeper_save_no_dive_not_held | 500 |
| min_delay_keeper_save_with_outreached_foot | 2000 |
| min_extra_delay_for_falling_down_before_injury | 4000 |

| Acceleration & Deceleration | Defaults |
|  ------- |  ------- |
| acceleration_scaler | 10000 |
| theoretical_min_acceleration | 2500 |
| theoretical_max_acceleration | 89408 |
| theoretical_min_deceleration | 15000 |
| theoretical_max_deceleration | 44704 |
| theoretical_min_diving_acceleration | 25000 |
| theoretical_max_diving_acceleration | 89408 |
| theoretical_min_diving_speed | 50000 |
| theoretical_max_diving_speed | 75000 |
| theoretical_max_running_speed | 122700  |

| Direction change | Defaults |
|  ------- |  ------- |
| theoretical_max_turning_rate | 180 |
| theoretical_min_potential_direction_change_walk | 52 |
| theoretical_max_potential_direction_change_walk | 192 |
| theoretical_min_potential_direction_change_jog | 15 |
| theoretical_max_potential_direction_change_jog | 104 |
| theoretical_min_potential_direction_change_run | 15 |
| theoretical_max_potential_direction_change_run | 53 |

| Movements | Defaults |
|  ------- |  ------- |
| speed_scaler | 10000 |
| very_slow_walk_speed | 4470 |
| slow_walk_speed | 8940 |
| walk_speed | 13410 |
| fast_walk_speed | 17880 |
| slow_jog_speed | 23000 |
| jog_speed | 26820 |
| moderate_jog_speed | 31290 |
| fast_jog_speed | 35760 |
| run_speed | 44704 |
| sprint_speed | 67056 |
| base_top_speed | 78000 |
| top_speed | 89408 |
| basic_header_speed | 120000  |

| Kick | Defaults |
|  ------- |  ------- |
| soft_kick_speed | 50000 |
| soft_to_medium_kick_speed | 90000 |
| medium_kick_speed | 130000  |
| medium_to_moderate_kick_speed | 180000  |
| moderate_kick_speed | 220000  |
| quite_hard_kick_speed | 270000  |
| hard_kick_speed | 310000  |
| very_hard_kick_speed | 350000  |
