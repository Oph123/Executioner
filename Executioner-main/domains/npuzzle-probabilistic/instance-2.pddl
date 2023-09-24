(
  define
  (problem instance-2)
  (:domain n-puzzle-typed)
  (:objects t_13 p_4_5 p_4_3 p_4_4 t_10 t_4 p_1_1 p_2_3 p_3_1 p_3_2 t_19 p_1_4 p_5_1 p_3_4 t_3 t_1 p_3_5 t_22 p_2_4 t_23 t_16 p_3_3 t_8 p_5_4 p_1_5 p_4_2 t_20 t_11 t_7 p_2_1 t_6 t_17 t_12 t_15 p_1_2 p_2_2 p_1_3 t_2 p_4_1 p_5_5 p_5_2 t_14 t_9 t_5 t_18 p_2_5 t_24 p_5_3 t_21)
  (
    :init
    (neighbor p_2_5 p_2_4)
    (neighbor p_4_5 p_4_4)
    (position_ p_5_5)
    (position_ p_5_4)
    (tile_____ t_21)
    (tile_____ t_9)
    (neighbor p_3_4 p_4_4)
    (neighbor p_5_1 p_4_1)
    (neighbor p_3_5 p_4_5)
    (position_ p_1_5)
    (neighbor p_4_3 p_4_4)
    (neighbor p_3_2 p_2_2)
    (at t_8 p_5_3)
    (at t_3 p_3_4)
    (neighbor p_1_1 p_2_1)
    (neighbor p_3_5 p_3_4)
    (position_ p_3_1)
    (neighbor p_4_5 p_5_5)
    (tile_____ t_19)
    (position_ p_2_5)
    (neighbor p_5_2 p_5_1)
    (position_ p_1_2)
    (at t_12 p_1_3)
    (neighbor p_2_2 p_3_2)
    (tile_____ t_20)
    (position_ p_2_4)
    (position_ p_5_2)
    (neighbor p_4_3 p_4_2)
    (position_ p_1_3)
    (position_ p_1_4)
    (at t_2 p_2_3)
    (neighbor p_5_3 p_5_4)
    (neighbor p_1_3 p_1_2)
    (neighbor p_4_4 p_3_4)
    (tile_____ t_10)
    (position_ p_5_1)
    (neighbor p_3_3 p_3_4)
    (neighbor p_5_4 p_4_4)
    (neighbor p_4_2 p_3_2)
    (position_ p_4_5)
    (neighbor p_1_3 p_1_4)
    (neighbor p_2_1 p_1_1)
    (neighbor p_1_4 p_1_3)
    (neighbor p_2_5 p_1_5)
    (neighbor p_3_2 p_3_1)
    (at t_6 p_2_1)
    (neighbor p_2_1 p_3_1)
    (neighbor p_3_3 p_3_2)
    (neighbor p_5_4 p_5_5)
    (at t_21 p_4_4)
    (at t_14 p_4_2)
    (at t_15 p_5_5)
    (position_ p_3_5)
    (neighbor p_2_4 p_2_5)
    (neighbor p_1_1 p_1_2)
    (at t_7 p_4_1)
    (neighbor p_5_2 p_5_3)
    (neighbor p_5_4 p_5_3)
    (position_ p_3_4)
    (neighbor p_3_1 p_4_1)
    (neighbor p_2_4 p_2_3)
    (neighbor p_4_1 p_5_1)
    (neighbor p_1_2 p_1_1)
    (neighbor p_2_4 p_1_4)
    (neighbor p_3_1 p_3_2)
    (at t_20 p_1_4)
    (neighbor p_5_1 p_5_2)
    (tile_____ t_22)
    (at t_23 p_3_2)
    (neighbor p_4_2 p_4_1)
    (neighbor p_2_2 p_2_1)
    (neighbor p_3_3 p_2_3)
    (neighbor p_4_3 p_5_3)
    (neighbor p_1_2 p_1_3)
    (tile_____ t_2)
    (neighbor p_3_4 p_3_5)
    (neighbor p_1_2 p_2_2)
    (neighbor p_4_2 p_4_3)
    (tile_____ t_15)
    (position_ p_3_2)
    (tile_____ t_7)
    (neighbor p_1_4 p_2_4)
    (neighbor p_3_1 p_2_1)
    (at t_13 p_5_4)
    (neighbor p_3_4 p_2_4)
    (at t_18 p_2_4)
    (at t_9 p_2_2)
    (neighbor p_4_1 p_3_1)
    (neighbor p_2_3 p_2_4)
    (neighbor p_4_4 p_4_3)
    (neighbor p_1_3 p_2_3)
    (tile_____ t_17)
    (neighbor p_4_4 p_4_5)
    (at t_24 p_4_5)
    (empty p_1_5)
    (at t_11 p_1_2)
    (neighbor p_5_3 p_4_3)
    (position_ p_2_3)
    (at t_10 p_5_1)
    (neighbor p_5_2 p_4_2)
    (tile_____ t_14)
    (neighbor p_5_5 p_4_5)
    (neighbor p_3_2 p_3_3)
    (neighbor p_2_4 p_3_4)
    (neighbor p_3_4 p_3_3)
    (position_ p_2_2)
    (tile_____ t_18)
    (neighbor p_1_5 p_2_5)
    (tile_____ t_6)
    (neighbor p_4_3 p_3_3)
    (neighbor p_2_3 p_3_3)
    (tile_____ t_23)
    (neighbor p_3_2 p_4_2)
    (tile_____ t_4)
    (tile_____ t_8)
    (tile_____ t_12)
    (position_ p_4_1)
    (neighbor p_1_5 p_1_4)
    (position_ p_5_3)
    (at t_1 p_3_5)
    (neighbor p_3_3 p_4_3)
    (position_ p_4_2)
    (neighbor p_2_2 p_1_2)
    (at t_4 p_3_1)
    (position_ p_4_3)
    (neighbor p_5_3 p_5_2)
    (tile_____ t_24)
    (tile_____ t_11)
    (neighbor p_3_5 p_2_5)
    (at t_17 p_4_3)
    (neighbor p_4_4 p_5_4)
    (tile_____ t_1)
    (position_ p_2_1)
    (neighbor p_1_4 p_1_5)
    (at t_19 p_2_5)
    (neighbor p_2_2 p_2_3)
    (tile_____ t_3)
    (tile_____ t_16)
    (position_ p_1_1)
    (at t_5 p_1_1)
    (neighbor p_5_5 p_5_4)
    (at t_22 p_5_2)
    (neighbor p_4_2 p_5_2)
    (position_ p_4_4)
    (tile_____ t_13)
    (neighbor p_2_1 p_2_2)
    (neighbor p_2_3 p_1_3)
    (neighbor p_2_3 p_2_2)
    (neighbor p_2_5 p_3_5)
    (neighbor p_4_5 p_3_5)
    (tile_____ t_5)
    (at t_16 p_3_3)
    (neighbor p_4_1 p_4_2)
    (position_ p_3_3)
    (injected-0)
  )
  (
    :goal
    (
      and
      (at t_1 p_1_1)
      (at t_2 p_1_2)
      (at t_3 p_1_3)
      (at t_4 p_1_4)
      (at t_5 p_1_5)
      (at t_6 p_2_1)
      (at t_7 p_2_2)
      (at t_8 p_2_3)
      (at t_9 p_2_4)
      (at t_10 p_2_5)
      (at t_11 p_3_1)
      (at t_12 p_3_2)
      (at t_13 p_3_3)
      (at t_14 p_3_4)
      (at t_15 p_3_5)
      (at t_16 p_4_1)
      (at t_17 p_4_2)
      (at t_18 p_4_3)
      (at t_19 p_4_4)
      (at t_20 p_4_5)
      (at t_21 p_5_1)
      (at t_22 p_5_2)
      (at t_23 p_5_3)
      (at t_24 p_5_4)
      (injected-0)
    )
  )
)