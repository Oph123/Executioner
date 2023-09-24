(
  define
  (domain ferry)
  (
    :predicates
    (location ?l)
    (empty-ferry)
    (on ?c)
    (car ?c)
    (at-ferry ?l)
    (at ?c ?l)
    (not-eq ?x ?y)
    (injected---0)
  )
  (
    :action
    sail
    :parameters
    (?from ?to)
    :precondition
    (
      and
      (not-eq ?from ?to)
      (location ?from)
      (location ?to)
      (at-ferry ?from)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (at-ferry ?to)
        (
          not
          (at-ferry ?from)
        )
      )
      0.18384683641971478
      (injected---0)
      0.26615316358028523
      (
        not
        (injected---0)
      )
    )
  )
  (
    :action
    debark
    :parameters
    (?car ?loc)
    :precondition
    (
      and
      (car ?car)
      (location ?loc)
      (on ?car)
      (at-ferry ?loc)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (at ?car ?loc)
        (empty-ferry)
        (
          not
          (on ?car)
        )
      )
      0.07356778731317386
      (injected---0)
      0.37643221268682614
      (
        not
        (injected---0)
      )
    )
  )
  (
    :action
    board
    :parameters
    (?car ?loc)
    :precondition
    (
      and
      (car ?car)
      (location ?loc)
      (at ?car ?loc)
      (at-ferry ?loc)
      (empty-ferry)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (on ?car)
        (
          not
          (at ?car ?loc)
        )
        (
          not
          (empty-ferry)
        )
      )
      0.06590822841354636
      (injected---0)
      0.38409177158645363
      (
        not
        (injected---0)
      )
    )
  )
)