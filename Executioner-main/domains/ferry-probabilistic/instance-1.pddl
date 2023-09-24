(
  define
  (problem instance-1)
  (:domain ferry)
  (:objects l0 c0 l1 c3 c1 l2 c2)
  (
    :init
    (location l0)
    (empty-ferry)
    (car c2)
    (not-eq l1 l2)
    (car c1)
    (at c0 l2)
    (at c2 l0)
    (at c3 l1)
    (car c3)
    (at c1 l0)
    (not-eq l2 l0)
    (location l1)
    (not-eq l1 l0)
    (not-eq l0 l1)
    (at-ferry l0)
    (location l2)
    (car c0)
    (not-eq l0 l2)
    (not-eq l2 l1)
    (injected---0)
  )
  (
    :goal
    (
      and
      (at c0 l1)
      (at c1 l1)
      (at c2 l0)
      (at c3 l2)
      (injected---0)
    )
  )
)