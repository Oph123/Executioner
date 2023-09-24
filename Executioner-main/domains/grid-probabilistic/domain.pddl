(
  define
  (domain grid)
  (
    :predicates
    (open ?x)
    (conn ?x ?y)
    (lock-shape ?x ?s)
    (holding ?k)
    (locked ?x)
    (at ?r ?x)
    (key-shape ?k ?s)
    (at-robot ?x)
    (key ?k)
    (shape ?s)
    (place ?p)
    (arm-empty)
    (injected--0)
  )
  (
    :action
    pickup
    :parameters
    (?curpos ?key)
    :precondition
    (
      and
      (place ?curpos)
      (key ?key)
      (at-robot ?curpos)
      (at ?key ?curpos)
      (arm-empty)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (holding ?key)
        (
          not
          (at ?key ?curpos)
        )
        (
          not
          (arm-empty)
        )
      )
      0.19204342023088403
      (injected--0)
      0.25795657976911607
      (
        not
        (injected--0)
      )
    )
  )
  (
    :action
    unlock
    :parameters
    (?curpos ?lockpos ?key ?shape)
    :precondition
    (
      and
      (place ?curpos)
      (place ?lockpos)
      (key ?key)
      (shape ?shape)
      (conn ?curpos ?lockpos)
      (key-shape ?key ?shape)
      (lock-shape ?lockpos ?shape)
      (at-robot ?curpos)
      (locked ?lockpos)
      (holding ?key)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (open ?lockpos)
        (
          not
          (locked ?lockpos)
        )
      )
      0.26827252950738983
      (injected--0)
      0.18172747049261018
      (
        not
        (injected--0)
      )
    )
  )
  (
    :action
    putdown
    :parameters
    (?curpos ?key)
    :precondition
    (
      and
      (place ?curpos)
      (key ?key)
      (at-robot ?curpos)
      (holding ?key)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (arm-empty)
        (at ?key ?curpos)
        (
          not
          (holding ?key)
        )
      )
      0.24713585363777427
      (injected--0)
      0.20286414636222572
      (
        not
        (injected--0)
      )
    )
  )
  (
    :action
    move
    :parameters
    (?curpos ?nextpos)
    :precondition
    (
      and
      (place ?curpos)
      (place ?nextpos)
      (at-robot ?curpos)
      (conn ?curpos ?nextpos)
      (open ?nextpos)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (at-robot ?nextpos)
        (
          not
          (at-robot ?curpos)
        )
      )
      0.27434975583317883
      (injected--0)
      0.17565024416682118
      (
        not
        (injected--0)
      )
    )
  )
  (
    :action
    pickup-and-loose
    :parameters
    (?curpos ?newkey ?oldkey)
    :precondition
    (
      and
      (place ?curpos)
      (key ?newkey)
      (key ?oldkey)
      (at-robot ?curpos)
      (holding ?oldkey)
      (at ?newkey ?curpos)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (holding ?newkey)
        (at ?oldkey ?curpos)
        (
          not
          (holding ?oldkey)
        )
        (
          not
          (at ?newkey ?curpos)
        )
      )
      0.3478974845900979
      (injected--0)
      0.10210251540990213
      (
        not
        (injected--0)
      )
    )
  )
)