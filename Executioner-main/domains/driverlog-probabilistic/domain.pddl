(
  define
  (domain driverlog)
  (
    :predicates
    (driving ?d ?v)
    (location ?x)
    (truck___ ?x)
    (empty ?v)
    (at ?obj ?loc)
    (link ?x ?y)
    (in ?obj1 ?obj)
    (path ?x ?y)
    (driver__ ?x)
    (locatable ?x)
    (obj_____ ?x)
    (injected-0)
  )
  (
    :action
    drive-truck
    :parameters
    (?truck ?loc-from ?loc-to ?driver)
    :precondition
    (
      and
      (at ?truck ?loc-from)
      (driving ?driver ?truck)
      (link ?loc-from ?loc-to)
      (truck___ ?truck)
      (location ?loc-from)
      (location ?loc-to)
      (driver__ ?driver)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (at ?truck ?loc-from)
        )
        (at ?truck ?loc-to)
      )
      0.19546447009490403
      (injected-0)
      0.254535529905096
      (
        not
        (injected-0)
      )
    )
  )
  (
    :action
    board-truck
    :parameters
    (?driver ?truck ?loc)
    :precondition
    (
      and
      (at ?truck ?loc)
      (at ?driver ?loc)
      (empty ?truck)
      (driver__ ?driver)
      (truck___ ?truck)
      (location ?loc)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (at ?driver ?loc)
        )
        (driving ?driver ?truck)
        (
          not
          (empty ?truck)
        )
      )
      0.2497880108040129
      (injected-0)
      0.2002119891959871
      (
        not
        (injected-0)
      )
    )
  )
  (
    :action
    walk
    :parameters
    (?driver ?loc-from ?loc-to)
    :precondition
    (
      and
      (at ?driver ?loc-from)
      (path ?loc-from ?loc-to)
      (driver__ ?driver)
      (location ?loc-from)
      (location ?loc-to)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (at ?driver ?loc-from)
        )
        (at ?driver ?loc-to)
      )
      0.12895739667226555
      (injected-0)
      0.3210426033277345
      (
        not
        (injected-0)
      )
    )
  )
  (
    :action
    load-truck
    :parameters
    (?obj ?truck ?loc)
    :precondition
    (
      and
      (at ?truck ?loc)
      (at ?obj ?loc)
      (obj_____ ?obj)
      (truck___ ?truck)
      (location ?loc)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (at ?obj ?loc)
        )
        (in ?obj ?truck)
      )
      0.2286941790070926
      (injected-0)
      0.22130582099290738
      (
        not
        (injected-0)
      )
    )
  )
  (
    :action
    unload-truck
    :parameters
    (?obj ?truck ?loc)
    :precondition
    (
      and
      (at ?truck ?loc)
      (in ?obj ?truck)
      (obj_____ ?obj)
      (truck___ ?truck)
      (location ?loc)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (in ?obj ?truck)
        )
        (at ?obj ?loc)
      )
      0.42025104283710457
      (injected-0)
      0.029748957162895443
      (
        not
        (injected-0)
      )
    )
  )
  (
    :action
    disembark-truck
    :parameters
    (?driver ?truck ?loc)
    :precondition
    (
      and
      (at ?truck ?loc)
      (driving ?driver ?truck)
      (driver__ ?driver)
      (truck___ ?truck)
      (location ?loc)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (driving ?driver ?truck)
        )
        (at ?driver ?loc)
        (empty ?truck)
      )
      0.23933679560406457
      (injected-0)
      0.21066320439593544
      (
        not
        (injected-0)
      )
    )
  )
)