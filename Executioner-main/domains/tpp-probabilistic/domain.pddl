(
  define
  (domain tpp-propositional)
  (
    :predicates
    (locatable_____ ?x)
    (stored ?g ?l)
    (level_________ ?x)
    (ready-to-load ?g ?m ?l)
    (depot_________ ?x)
    (truck_________ ?x)
    (on-sale ?g ?m ?l)
    (market________ ?x)
    (loaded ?g ?t ?l)
    (at ?t ?p)
    (connected ?p1 ?p2)
    (next ?l1 ?l2)
    (goods_________ ?x)
    (place_________ ?x)
    (injected------0)
  )
  (
    :action
    buy
    :parameters
    (?t ?g ?m ?l1 ?l2 ?l3 ?l4)
    :precondition
    (
      and
      (at ?t ?m)
      (on-sale ?g ?m ?l2)
      (ready-to-load ?g ?m ?l3)
      (next ?l2 ?l1)
      (next ?l4 ?l3)
      (truck_________ ?t)
      (goods_________ ?g)
      (market________ ?m)
      (level_________ ?l1)
      (level_________ ?l2)
      (level_________ ?l3)
      (level_________ ?l4)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (on-sale ?g ?m ?l1)
        (
          not
          (on-sale ?g ?m ?l2)
        )
        (ready-to-load ?g ?m ?l4)
        (
          not
          (ready-to-load ?g ?m ?l3)
        )
      )
      0.3079264131848908
      (injected------0)
      0.1420735868151093
      (
        not
        (injected------0)
      )
    )
  )
  (
    :action
    unload
    :parameters
    (?g ?t ?d ?l1 ?l2 ?l3 ?l4)
    :precondition
    (
      and
      (at ?t ?d)
      (loaded ?g ?t ?l2)
      (stored ?g ?l3)
      (next ?l2 ?l1)
      (next ?l4 ?l3)
      (goods_________ ?g)
      (truck_________ ?t)
      (depot_________ ?d)
      (level_________ ?l1)
      (level_________ ?l2)
      (level_________ ?l3)
      (level_________ ?l4)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (loaded ?g ?t ?l1)
        (
          not
          (loaded ?g ?t ?l2)
        )
        (stored ?g ?l4)
        (
          not
          (stored ?g ?l3)
        )
      )
      0.18372412739715913
      (injected------0)
      0.26627587260284086
      (
        not
        (injected------0)
      )
    )
  )
  (
    :action
    load
    :parameters
    (?g ?t ?m ?l1 ?l2 ?l3 ?l4)
    :precondition
    (
      and
      (at ?t ?m)
      (loaded ?g ?t ?l3)
      (ready-to-load ?g ?m ?l2)
      (next ?l2 ?l1)
      (next ?l4 ?l3)
      (goods_________ ?g)
      (truck_________ ?t)
      (market________ ?m)
      (level_________ ?l1)
      (level_________ ?l2)
      (level_________ ?l3)
      (level_________ ?l4)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (loaded ?g ?t ?l4)
        (
          not
          (loaded ?g ?t ?l3)
        )
        (ready-to-load ?g ?m ?l1)
        (
          not
          (ready-to-load ?g ?m ?l2)
        )
      )
      0.18130824994240183
      (injected------0)
      0.2686917500575982
      (
        not
        (injected------0)
      )
    )
  )
  (
    :action
    drive
    :parameters
    (?t ?from ?to)
    :precondition
    (
      and
      (at ?t ?from)
      (connected ?from ?to)
      (truck_________ ?t)
      (place_________ ?from)
      (place_________ ?to)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (at ?t ?from)
        )
        (at ?t ?to)
      )
      0.2800272605355831
      (injected------0)
      0.16997273946441696
      (
        not
        (injected------0)
      )
    )
  )
)