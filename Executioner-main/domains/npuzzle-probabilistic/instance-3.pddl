(
  define
  (problem instance-3)
  (:domain n-puzzle-typed)
  (:objects t_13 p_4_3 p_6_4 p_2_3 p_6_1 t_19 p_5_1 p_3_4 t_3 t_1 p_2_4 t_23 t_33 t_16 t_8 p_1_5 p_3_6 p_6_5 p_6_6 t_11 p_6_3 t_6 t_28 t_15 p_1_2 p_2_2 p_1_3 t_2 p_4_1 p_5_2 t_14 t_18 p_5_3 t_21 p_4_5 p_4_4 t_10 t_4 t_25 t_30 p_1_1 p_3_1 t_29 p_3_2 p_1_4 t_26 p_3_5 t_22 p_1_6 t_31 p_3_3 p_5_4 t_35 p_4_2 t_20 p_5_6 t_27 p_6_2 t_7 p_2_1 t_17 t_12 t_32 p_2_6 p_5_5 t_34 t_9 t_5 p_2_5 t_24 p_4_6)
  (
    :init
    (neighbor p_4_5 p_4_6)
    (position_ p_2_6)
    (neighbor p_2_5 p_2_4)
    (neighbor p_4_5 p_4_4)
    (position_ p_5_5)
    (neighbor p_1_5 p_1_6)
    (tile_____ t_21)
    (position_ p_5_4)
    (tile_____ t_9)
    (neighbor p_3_4 p_4_4)
    (at t_26 p_3_5)
    (neighbor p_5_1 p_4_1)
    (neighbor p_3_5 p_4_5)
    (position_ p_1_5)
    (neighbor p_4_3 p_4_4)
    (neighbor p_2_6 p_2_5)
    (neighbor p_3_2 p_2_2)
    (neighbor p_6_2 p_6_3)
    (neighbor p_4_6 p_3_6)
    (neighbor p_5_1 p_6_1)
    (neighbor p_1_1 p_2_1)
    (at t_31 p_1_6)
    (at t_27 p_2_4)
    (neighbor p_6_1 p_6_2)
    (neighbor p_3_5 p_3_4)
    (tile_____ t_33)
    (neighbor p_4_5 p_5_5)
    (position_ p_3_1)
    (at t_20 p_2_1)
    (neighbor p_6_2 p_5_2)
    (tile_____ t_19)
    (tile_____ t_25)
    (position_ p_2_5)
    (neighbor p_5_5 p_5_6)
    (neighbor p_5_2 p_5_1)
    (position_ p_1_2)
    (at t_19 p_3_4)
    (neighbor p_1_6 p_2_6)
    (neighbor p_3_5 p_3_6)
    (neighbor p_2_2 p_3_2)
    (tile_____ t_20)
    (position_ p_2_4)
    (position_ p_5_2)
    (neighbor p_4_3 p_4_2)
    (at t_16 p_1_4)
    (at t_3 p_3_2)
    (position_ p_1_3)
    (neighbor p_5_6 p_4_6)
    (position_ p_1_4)
    (neighbor p_5_3 p_5_4)
    (neighbor p_6_4 p_5_4)
    (at t_14 p_6_4)
    (neighbor p_1_3 p_1_2)
    (neighbor p_4_4 p_3_4)
    (at t_21 p_4_3)
    (position_ p_5_1)
    (at t_25 p_1_5)
    (tile_____ t_10)
    (neighbor p_3_3 p_3_4)
    (neighbor p_5_4 p_4_4)
    (neighbor p_6_3 p_6_2)
    (neighbor p_6_5 p_5_5)
    (at t_11 p_4_2)
    (neighbor p_4_2 p_3_2)
    (neighbor p_5_6 p_6_6)
    (neighbor p_3_6 p_2_6)
    (neighbor p_6_3 p_6_4)
    (neighbor p_1_3 p_1_4)
    (at t_2 p_5_6)
    (empty p_6_6)
    (neighbor p_2_1 p_1_1)
    (at t_24 p_3_6)
    (position_ p_4_5)
    (neighbor p_1_4 p_1_3)
    (neighbor p_5_3 p_6_3)
    (neighbor p_6_4 p_6_3)
    (neighbor p_2_5 p_1_5)
    (at t_23 p_3_1)
    (neighbor p_3_2 p_3_1)
    (position_ p_3_3)
    (at t_33 p_2_2)
    (neighbor p_2_1 p_3_1)
    (neighbor p_3_3 p_3_2)
    (neighbor p_5_4 p_5_5)
    (position_ p_3_5)
    (neighbor p_6_5 p_6_6)
    (at t_1 p_3_3)
    (at t_28 p_5_3)
    (neighbor p_2_6 p_1_6)
    (at t_6 p_4_4)
    (neighbor p_1_1 p_1_2)
    (neighbor p_2_4 p_2_5)
    (neighbor p_4_6 p_4_5)
    (tile_____ t_35)
    (position_ p_4_6)
    (neighbor p_5_2 p_5_3)
    (neighbor p_6_3 p_5_3)
    (neighbor p_6_1 p_5_1)
    (neighbor p_5_4 p_5_3)
    (neighbor p_2_6 p_3_6)
    (position_ p_3_4)
    (neighbor p_3_1 p_4_1)
    (neighbor p_2_4 p_2_3)
    (neighbor p_4_1 p_5_1)
    (neighbor p_1_2 p_1_1)
    (position_ p_1_6)
    (neighbor p_6_4 p_6_5)
    (neighbor p_2_4 p_1_4)
    (neighbor p_3_1 p_3_2)
    (at t_9 p_6_5)
    (at t_30 p_2_5)
    (neighbor p_5_1 p_5_2)
    (neighbor p_4_2 p_4_1)
    (neighbor p_2_2 p_2_1)
    (neighbor p_5_6 p_5_5)
    (tile_____ t_22)
    (neighbor p_3_3 p_2_3)
    (neighbor p_4_3 p_5_3)
    (neighbor p_1_2 p_1_3)
    (tile_____ t_2)
    (neighbor p_3_4 p_3_5)
    (neighbor p_1_2 p_2_2)
    (neighbor p_6_6 p_6_5)
    (neighbor p_4_2 p_4_3)
    (tile_____ t_15)
    (position_ p_3_2)
    (tile_____ t_7)
    (neighbor p_1_4 p_2_4)
    (neighbor p_3_1 p_2_1)
    (position_ p_6_1)
    (tile_____ t_29)
    (tile_____ t_31)
    (neighbor p_5_4 p_6_4)
    (neighbor p_3_4 p_2_4)
    (at t_12 p_5_4)
    (at t_17 p_6_1)
    (neighbor p_4_1 p_3_1)
    (neighbor p_2_3 p_2_4)
    (neighbor p_4_4 p_4_3)
    (neighbor p_1_3 p_2_3)
    (at t_15 p_5_1)
    (tile_____ t_17)
    (at t_4 p_6_2)
    (position_ p_6_5)
    (at t_35 p_2_3)
    (neighbor p_4_4 p_4_5)
    (position_ p_6_3)
    (tile_____ t_28)
    (at t_29 p_1_2)
    (at t_18 p_2_6)
    (position_ p_6_4)
    (neighbor p_3_6 p_3_5)
    (neighbor p_5_3 p_4_3)
    (neighbor p_1_6 p_1_5)
    (position_ p_2_3)
    (neighbor p_5_2 p_4_2)
    (tile_____ t_14)
    (neighbor p_5_5 p_4_5)
    (neighbor p_3_2 p_3_3)
    (tile_____ t_27)
    (neighbor p_2_4 p_3_4)
    (neighbor p_3_4 p_3_3)
    (neighbor p_3_6 p_4_6)
    (position_ p_2_2)
    (neighbor p_1_5 p_2_5)
    (tile_____ t_18)
    (tile_____ t_6)
    (neighbor p_4_3 p_3_3)
    (neighbor p_2_3 p_3_3)
    (position_ p_6_6)
    (tile_____ t_23)
    (neighbor p_3_2 p_4_2)
    (tile_____ t_4)
    (neighbor p_6_2 p_6_1)
    (tile_____ t_8)
    (tile_____ t_12)
    (position_ p_4_1)
    (tile_____ t_32)
    (neighbor p_6_6 p_5_6)
    (neighbor p_1_5 p_1_4)
    (position_ p_5_3)
    (neighbor p_3_3 p_4_3)
    (tile_____ t_26)
    (position_ p_4_2)
    (neighbor p_2_2 p_1_2)
    (at t_13 p_4_1)
    (position_ p_4_3)
    (neighbor p_5_3 p_5_2)
    (tile_____ t_24)
    (tile_____ t_11)
    (neighbor p_3_5 p_2_5)
    (neighbor p_2_5 p_2_6)
    (neighbor p_4_4 p_5_4)
    (neighbor p_5_2 p_6_2)
    (position_ p_5_6)
    (at t_8 p_5_5)
    (tile_____ t_1)
    (position_ p_2_1)
    (neighbor p_1_4 p_1_5)
    (at t_7 p_1_3)
    (neighbor p_2_2 p_2_3)
    (neighbor p_6_5 p_6_4)
    (tile_____ t_3)
    (tile_____ t_16)
    (position_ p_1_1)
    (at t_5 p_1_1)
    (tile_____ t_34)
    (neighbor p_5_5 p_6_5)
    (neighbor p_5_5 p_5_4)
    (at t_22 p_5_2)
    (neighbor p_4_2 p_5_2)
    (position_ p_4_4)
    (at t_32 p_6_3)
    (tile_____ t_13)
    (neighbor p_2_1 p_2_2)
    (neighbor p_2_3 p_1_3)
    (tile_____ t_30)
    (position_ p_6_2)
    (neighbor p_2_3 p_2_2)
    (neighbor p_4_6 p_5_6)
    (neighbor p_2_5 p_3_5)
    (neighbor p_4_5 p_3_5)
    (tile_____ t_5)
    (at t_34 p_4_6)
    (neighbor p_4_1 p_4_2)
    (position_ p_3_6)
    (at t_10 p_4_5)
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
      (at t_6 p_1_6)
      (at t_7 p_2_1)
      (at t_8 p_2_2)
      (at t_9 p_2_3)
      (at t_10 p_2_4)
      (at t_11 p_2_5)
      (at t_12 p_2_6)
      (at t_13 p_3_1)
      (at t_14 p_3_2)
      (at t_15 p_3_3)
      (at t_16 p_3_4)
      (at t_17 p_3_5)
      (at t_18 p_3_6)
      (at t_19 p_4_1)
      (at t_20 p_4_2)
      (at t_21 p_4_3)
      (at t_22 p_4_4)
      (at t_23 p_4_5)
      (at t_24 p_4_6)
      (at t_25 p_5_1)
      (at t_26 p_5_2)
      (at t_27 p_5_3)
      (at t_28 p_5_4)
      (at t_29 p_5_5)
      (at t_30 p_5_6)
      (at t_31 p_6_1)
      (at t_32 p_6_2)
      (at t_33 p_6_3)
      (at t_34 p_6_4)
      (at t_35 p_6_5)
      (injected-0)
    )
  )
)