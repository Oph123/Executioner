(
  define
  (domain hanoi)
  (
    :predicates
    (on ?x ?y)
    (smaller ?x ?y)
    (clear ?x)
    (injected-0)
  )
  (
    :action
    move
    :parameters
    (?disc ?from ?to)
    :precondition
    (
      and
      (smaller ?to ?disc)
      (on ?disc ?from)
      (clear ?disc)
      (clear ?to)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (clear ?from)
        (on ?disc ?to)
        (
          not
          (on ?disc ?from)
        )
        (
          not
          (clear ?to)
        )
      )
      0.2689271540562672
      (injected-0)
      0.18107284594373277
      (
        not
        (injected-0)
      )
    )
  )
)