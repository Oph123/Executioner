(
  define
  (problem instance-4)
  (:domain satellite)
  (:objects star17 instrument1 infrared3 groundstation2 instrument4 instrument2 instrument7 planet16 infrared0 groundstation4 star5 groundstation8 instrument8 planet15 instrument0 image2 instrument5 satellite1 groundstation0 star11 groundstation6 satellite0 satellite2 star3 groundstation10 groundstation1 phenomenon12 phenomenon13 groundstation9 planet14 star7 image1 instrument3 instrument6)
  (
    :init
    (direction__________ groundstation10)
    (calibration_target instrument6 groundstation8)
    (on_board instrument3 satellite1)
    (direction__________ planet15)
    (calibration_target instrument3 star5)
    (instrument_________ instrument0)
    (direction__________ star11)
    (pointing satellite0 planet14)
    (satellite__________ satellite1)
    (mode_______________ image1)
    (supports instrument4 image1)
    (instrument_________ instrument1)
    (supports instrument4 image2)
    (calibration_target instrument7 groundstation1)
    (direction__________ groundstation1)
    (direction__________ groundstation9)
    (on_board instrument2 satellite0)
    (on_board instrument5 satellite1)
    (calibration_target instrument1 groundstation0)
    (direction__________ phenomenon13)
    (supports instrument5 infrared3)
    (calibration_target instrument8 star5)
    (pointing satellite2 planet16)
    (power_avail satellite0)
    (power_avail satellite2)
    (pointing satellite1 groundstation1)
    (direction__________ star3)
    (direction__________ groundstation8)
    (calibration_target instrument2 groundstation8)
    (supports instrument1 infrared3)
    (calibration_target instrument3 groundstation1)
    (instrument_________ instrument3)
    (direction__________ star5)
    (on_board instrument0 satellite0)
    (calibration_target instrument2 groundstation10)
    (on_board instrument6 satellite2)
    (supports instrument7 infrared0)
    (satellite__________ satellite0)
    (satellite__________ satellite2)
    (direction__________ phenomenon12)
    (mode_______________ infrared3)
    (mode_______________ infrared0)
    (on_board instrument1 satellite0)
    (supports instrument4 infrared3)
    (instrument_________ instrument2)
    (supports instrument7 image1)
    (instrument_________ instrument4)
    (on_board instrument8 satellite2)
    (direction__________ planet16)
    (supports instrument8 image1)
    (direction__________ star17)
    (direction__________ star7)
    (direction__________ groundstation4)
    (on_board instrument7 satellite2)
    (instrument_________ instrument7)
    (direction__________ groundstation6)
    (direction__________ planet14)
    (calibration_target instrument6 groundstation2)
    (calibration_target instrument7 groundstation0)
    (calibration_target instrument4 star7)
    (supports instrument3 image1)
    (supports instrument6 image1)
    (instrument_________ instrument6)
    (supports instrument0 infrared3)
    (calibration_target instrument2 groundstation0)
    (supports instrument0 infrared0)
    (calibration_target instrument5 star7)
    (instrument_________ instrument5)
    (instrument_________ instrument8)
    (calibration_target instrument1 star5)
    (calibration_target instrument0 groundstation4)
    (direction__________ groundstation0)
    (supports instrument8 infrared3)
    (calibration_target instrument8 groundstation10)
    (supports instrument2 infrared3)
    (mode_______________ image2)
    (on_board instrument4 satellite1)
    (power_avail satellite1)
    (direction__________ groundstation2)
    (injected-----------0)
  )
  (
    :goal
    (
      and
      (pointing satellite0 star7)
      (pointing satellite1 planet15)
      (pointing satellite2 planet15)
      (have_image star11 image1)
      (have_image phenomenon12 image1)
      (have_image phenomenon13 infrared3)
      (have_image planet14 image2)
      (have_image planet15 infrared0)
      (have_image planet16 infrared3)
      (have_image star17 image1)
      (injected-----------0)
    )
  )
)