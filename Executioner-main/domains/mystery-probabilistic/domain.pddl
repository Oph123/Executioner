(
  define
  (domain mystery-strips)
  (
    :predicates
    (harmony ?v ?s)
    (craves ?v ?n)
    (planet ?x)
    (food ?x)
    (fears ?c ?v)
    (attacks ?i ?j)
    (eats ?n1 ?n2)
    (pleasure ?x)
    (locale ?n ?a)
    (province ?x)
    (pain ?x)
    (orbits ?i ?j)
    (injected-0)
  )
  (
    :action
    feast
    :parameters
    (?v ?n1 ?n2 ?l1 ?l2)
    :precondition
    (
      and
      (craves ?v ?n1)
      (food ?n1)
      (pleasure ?v)
      (eats ?n1 ?n2)
      (food ?n2)
      (locale ?n1 ?l2)
      (attacks ?l1 ?l2)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (craves ?v ?n1)
        )
        (craves ?v ?n2)
        (
          not
          (locale ?n1 ?l2)
        )
        (locale ?n1 ?l1)
      )
      0.21576230311011113
      (injected-0)
      0.2342376968898889
      (
        not
        (injected-0)
      )
    )
  )
  (
    :action
    overcome
    :parameters
    (?c ?v ?n ?s1 ?s2)
    :precondition
    (
      and
      (pain ?c)
      (pleasure ?v)
      (craves ?c ?n)
      (craves ?v ?n)
      (food ?n)
      (harmony ?v ?s2)
      (planet ?s2)
      (orbits ?s1 ?s2)
      (planet ?s1)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (craves ?c ?n)
        )
        (fears ?c ?v)
        (
          not
          (harmony ?v ?s2)
        )
        (harmony ?v ?s1)
      )
      0.18925264098846223
      (injected-0)
      0.2607473590115377
      (
        not
        (injected-0)
      )
    )
  )
  (
    :action
    succumb
    :parameters
    (?c ?v ?n ?s1 ?s2)
    :precondition
    (
      and
      (fears ?c ?v)
      (pain ?c)
      (pleasure ?v)
      (craves ?v ?n)
      (food ?n)
      (harmony ?v ?s1)
      (orbits ?s1 ?s2)
    )
    :effect
    (
      probabilistic
      0.5
      (
        and
        (
          not
          (fears ?c ?v)
        )
        (craves ?c ?n)
        (
          not
          (harmony ?v ?s1)
        )
        (harmony ?v ?s2)
      )
      0.2358984621261153
      (injected-0)
      0.2141015378738847
      (
        not
        (injected-0)
      )
    )
  )
)