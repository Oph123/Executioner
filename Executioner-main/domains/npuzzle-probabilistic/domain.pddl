(
  define
  (domain n-puzzle-typed)
  (
    :predicates
    (neighbor ?p1 ?p2)
    (position_ ?x)
    (tile_____ ?x)
    (at ?tile ?position)
    (empty ?position)
    (injected-0)
  )
  (
    :action
    move
    :parameters
    (?tile ?from ?to)
    :precondition
    (
      and
      (neighbor ?from ?to)
      (at ?tile ?from)
      (empty ?to)
      (tile_____ ?tile)
      (position_ ?from)
      (position_ ?to)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (at ?tile ?to)
        (empty ?from)
        (
          not
          (at ?tile ?from)
        )
        (
          not
          (empty ?to)
        )
      )
      0.30154011205741377
      (injected-0)
      0.14845988794258627
      (
        not
        (injected-0)
      )
    )
  )
)