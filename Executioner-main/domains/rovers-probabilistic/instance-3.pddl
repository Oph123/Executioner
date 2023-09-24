(
  define
  (problem instance-3)
  (:domain rover)
  (:objects waypoint0 camera4 rover4store rover3 camera1 camera2 rover4 camera3 objective0 camera0 rover2store high_res rover0 waypoint5 rover1store colour waypoint6 camera5 rover1 low_res waypoint7 waypoint1 general rover2 waypoint3 objective1 rover3store objective2 objective3 waypoint2 waypoint4 rover0store)
  (
    :init
    (can_traverse rover0 waypoint0 waypoint1)
    (can_traverse rover3 waypoint3 waypoint6)
    (at rover2 waypoint5)
    (visible waypoint0 waypoint3)
    (visible waypoint3 waypoint7)
    (visible waypoint2 waypoint1)
    (camera_____________________ camera1)
    (equipped_for_imaging rover3)
    (supports camera5 low_res)
    (available rover3)
    (can_traverse rover0 waypoint6 waypoint7)
    (at rover1 waypoint6)
    (at_soil_sample waypoint7)
    (visible waypoint6 waypoint0)
    (can_traverse rover2 waypoint4 waypoint5)
    (can_traverse rover3 waypoint0 waypoint3)
    (calibration_target camera2 objective3)
    (waypoint___________________ waypoint7)
    (can_traverse rover0 waypoint2 waypoint5)
    (on_board camera3 rover4)
    (can_traverse rover1 waypoint5 waypoint6)
    (on_board camera4 rover4)
    (can_traverse rover3 waypoint4 waypoint3)
    (visible_from objective3 waypoint1)
    (visible_from objective3 waypoint2)
    (camera_____________________ camera2)
    (supports camera3 low_res)
    (mode_______________________ colour)
    (can_traverse rover1 waypoint6 waypoint5)
    (rover______________________ rover3)
    (empty rover0store)
    (at_rock_sample waypoint6)
    (can_traverse rover3 waypoint5 waypoint0)
    (on_board camera5 rover2)
    (visible_from objective3 waypoint4)
    (can_traverse rover3 waypoint0 waypoint1)
    (can_traverse rover2 waypoint0 waypoint5)
    (at_rock_sample waypoint2)
    (can_traverse rover1 waypoint4 waypoint3)
    (visible waypoint1 waypoint3)
    (equipped_for_imaging rover4)
    (available rover4)
    (visible_from objective1 waypoint4)
    (calibration_target camera0 objective1)
    (supports camera5 colour)
    (store_of rover4store rover4)
    (can_traverse rover4 waypoint7 waypoint5)
    (waypoint___________________ waypoint4)
    (can_traverse rover3 waypoint3 waypoint0)
    (at rover0 waypoint6)
    (can_traverse rover0 waypoint7 waypoint6)
    (store______________________ rover0store)
    (visible waypoint3 waypoint6)
    (objective__________________ objective0)
    (can_traverse rover3 waypoint6 waypoint3)
    (visible waypoint5 waypoint0)
    (supports camera4 high_res)
    (can_traverse rover1 waypoint0 waypoint6)
    (can_traverse rover4 waypoint0 waypoint5)
    (visible waypoint5 waypoint3)
    (can_traverse rover3 waypoint7 waypoint3)
    (equipped_for_imaging rover1)
    (available rover1)
    (visible waypoint7 waypoint6)
    (visible waypoint1 waypoint0)
    (empty rover2store)
    (visible waypoint0 waypoint5)
    (can_traverse rover2 waypoint3 waypoint5)
    (store_of rover2store rover2)
    (visible waypoint3 waypoint0)
    (visible waypoint5 waypoint2)
    (visible waypoint5 waypoint1)
    (can_traverse rover2 waypoint0 waypoint1)
    (visible_from objective0 waypoint3)
    (can_traverse rover0 waypoint3 waypoint0)
    (available rover2)
    (can_traverse rover4 waypoint5 waypoint6)
    (supports camera0 colour)
    (at_rock_sample waypoint3)
    (camera_____________________ camera4)
    (visible waypoint6 waypoint3)
    (on_board camera1 rover1)
    (visible_from objective0 waypoint6)
    (visible waypoint2 waypoint7)
    (visible waypoint5 waypoint4)
    (visible waypoint6 waypoint5)
    (can_traverse rover2 waypoint1 waypoint0)
    (supports camera1 high_res)
    (can_traverse rover2 waypoint6 waypoint0)
    (store______________________ rover2store)
    (can_traverse rover2 waypoint5 waypoint2)
    (at rover3 waypoint3)
    (can_traverse rover3 waypoint1 waypoint0)
    (objective__________________ objective3)
    (visible_from objective2 waypoint3)
    (store______________________ rover1store)
    (visible waypoint1 waypoint5)
    (store_of rover3store rover3)
    (calibration_target camera3 objective3)
    (visible_from objective0 waypoint0)
    (calibration_target camera1 objective1)
    (supports camera3 colour)
    (rover______________________ rover4)
    (visible waypoint3 waypoint5)
    (supports camera4 colour)
    (lander_____________________ general)
    (visible_from objective2 waypoint2)
    (visible waypoint0 waypoint2)
    (visible waypoint0 waypoint1)
    (available rover0)
    (can_traverse rover0 waypoint0 waypoint3)
    (visible waypoint0 waypoint6)
    (can_traverse rover0 waypoint0 waypoint6)
    (visible waypoint7 waypoint5)
    (on_board camera2 rover3)
    (rover______________________ rover0)
    (equipped_for_soil_analysis rover3)
    (can_traverse rover2 waypoint5 waypoint0)
    (can_traverse rover1 waypoint3 waypoint6)
    (supports camera2 high_res)
    (visible_from objective3 waypoint3)
    (mode_______________________ high_res)
    (can_traverse rover3 waypoint3 waypoint4)
    (rover______________________ rover1)
    (empty rover1store)
    (can_traverse rover0 waypoint5 waypoint6)
    (equipped_for_imaging rover2)
    (empty rover4store)
    (at_rock_sample waypoint4)
    (visible waypoint5 waypoint6)
    (visible_from objective0 waypoint5)
    (can_traverse rover0 waypoint5 waypoint2)
    (visible_from objective1 waypoint3)
    (waypoint___________________ waypoint0)
    (visible waypoint1 waypoint2)
    (can_traverse rover4 waypoint5 waypoint7)
    (rover______________________ rover2)
    (can_traverse rover1 waypoint3 waypoint4)
    (camera_____________________ camera0)
    (can_traverse rover2 waypoint2 waypoint5)
    (visible_from objective1 waypoint6)
    (waypoint___________________ waypoint3)
    (visible waypoint5 waypoint7)
    (can_traverse rover3 waypoint0 waypoint5)
    (calibration_target camera5 objective3)
    (can_traverse rover0 waypoint5 waypoint4)
    (visible waypoint3 waypoint1)
    (visible waypoint7 waypoint3)
    (visible waypoint2 waypoint0)
    (can_traverse rover0 waypoint6 waypoint5)
    (visible waypoint1 waypoint4)
    (supports camera2 low_res)
    (visible waypoint4 waypoint3)
    (at_soil_sample waypoint6)
    (waypoint___________________ waypoint6)
    (camera_____________________ camera5)
    (can_traverse rover4 waypoint5 waypoint0)
    (can_traverse rover2 waypoint5 waypoint4)
    (visible waypoint3 waypoint4)
    (calibration_target camera4 objective3)
    (visible waypoint4 waypoint5)
    (store______________________ rover4store)
    (waypoint___________________ waypoint1)
    (waypoint___________________ waypoint2)
    (at rover4 waypoint5)
    (can_traverse rover4 waypoint5 waypoint3)
    (can_traverse rover0 waypoint4 waypoint5)
    (visible waypoint7 waypoint2)
    (visible waypoint7 waypoint1)
    (visible waypoint6 waypoint7)
    (can_traverse rover4 waypoint1 waypoint0)
    (objective__________________ objective1)
    (equipped_for_soil_analysis rover0)
    (empty rover3store)
    (at_lander general waypoint6)
    (can_traverse rover1 waypoint6 waypoint0)
    (can_traverse rover1 waypoint1 waypoint3)
    (can_traverse rover0 waypoint6 waypoint0)
    (can_traverse rover0 waypoint1 waypoint0)
    (can_traverse rover4 waypoint2 waypoint5)
    (equipped_for_soil_analysis rover1)
    (can_traverse rover4 waypoint5 waypoint2)
    (can_traverse rover1 waypoint6 waypoint3)
    (camera_____________________ camera3)
    (visible_from objective0 waypoint2)
    (visible_from objective0 waypoint1)
    (visible waypoint2 waypoint5)
    (supports camera0 high_res)
    (can_traverse rover4 waypoint6 waypoint5)
    (equipped_for_soil_analysis rover2)
    (store_of rover1store rover1)
    (store______________________ rover3store)
    (can_traverse rover2 waypoint0 waypoint6)
    (can_traverse rover1 waypoint3 waypoint1)
    (objective__________________ objective2)
    (can_traverse rover3 waypoint3 waypoint7)
    (visible waypoint4 waypoint1)
    (store_of rover0store rover0)
    (can_traverse rover2 waypoint5 waypoint3)
    (channel_free general)
    (on_board camera0 rover4)
    (can_traverse rover4 waypoint3 waypoint5)
    (supports camera0 low_res)
    (at_soil_sample waypoint5)
    (waypoint___________________ waypoint5)
    (mode_______________________ low_res)
    (can_traverse rover4 waypoint0 waypoint1)
    (visible waypoint1 waypoint7)
    (injected-------------------0)
  )
  (
    :goal
    (
      and
      (communicated_soil_data waypoint7)
      (communicated_soil_data waypoint6)
      (communicated_soil_data waypoint5)
      (communicated_image_data objective0 high_res)
      (communicated_image_data objective3 high_res)
      (communicated_image_data objective2 low_res)
      (communicated_image_data objective2 colour)
      (communicated_image_data objective1 colour)
      (communicated_image_data objective3 low_res)
      (injected-------------------0)
    )
  )
)