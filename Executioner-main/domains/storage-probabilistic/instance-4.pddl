(
  define
  (problem instance-4)
  (:domain storage-propositional)
  (:objects container0 container-0-0 hoist1 depot48-1-3 depot48-1-1 container-0-1 depot48-1-2 depot48-2-3 hoist2 depot48-1-4 crate3 depot48-2-4 crate2 container-0-3 depot48 crate0 loadarea container-0-2 crate1 depot48-2-1 depot48-2-2 hoist0)
  (
    :init
    (storearea__ depot48-1-1)
    (connected depot48-2-2 depot48-2-3)
    (clear depot48-1-1)
    (surface____ loadarea)
    (hoist______ hoist1)
    (in crate2 container0)
    (available hoist1)
    (hoist______ hoist2)
    (on crate3 container-0-3)
    (connected loadarea depot48-2-1)
    (surface____ crate3)
    (connected depot48-1-4 depot48-2-4)
    (storearea__ depot48-1-3)
    (connected depot48-2-3 depot48-1-3)
    (transitarea loadarea)
    (storearea__ depot48-1-4)
    (area_______ depot48-2-2)
    (connected loadarea container-0-3)
    (area_______ depot48-1-2)
    (storearea__ depot48-2-3)
    (clear depot48-2-3)
    (connected depot48-1-1 depot48-2-1)
    (surface____ crate1)
    (in container-0-0 container0)
    (area_______ depot48-2-1)
    (connected container-0-0 loadarea)
    (connected loadarea container-0-1)
    (in depot48-2-3 depot48)
    (at hoist0 depot48-2-1)
    (connected depot48-1-4 depot48-1-3)
    (container__ container0)
    (storearea__ container-0-0)
    (in container-0-2 container0)
    (connected depot48-1-3 depot48-1-2)
    (surface____ depot48-2-4)
    (crate______ crate0)
    (area_______ loadarea)
    (connected depot48-1-2 depot48-2-2)
    (connected depot48-2-2 depot48-1-2)
    (connected container-0-2 loadarea)
    (available hoist0)
    (connected depot48-2-1 depot48-2-2)
    (in container-0-1 container0)
    (in depot48-2-4 depot48)
    (in depot48-1-3 depot48)
    (surface____ container-0-3)
    (storearea__ depot48-2-2)
    (in depot48-1-1 depot48)
    (connected container-0-1 loadarea)
    (in depot48-2-2 depot48)
    (storearea__ depot48-1-2)
    (connected depot48-2-1 loadarea)
    (surface____ depot48-2-1)
    (connected depot48-2-4 depot48-1-4)
    (at hoist2 depot48-1-3)
    (connected depot48-1-3 depot48-1-4)
    (connected container-0-3 loadarea)
    (in depot48-2-1 depot48)
    (crate______ crate3)
    (connected depot48-2-3 depot48-2-4)
    (area_______ depot48-2-4)
    (surface____ container-0-1)
    (connected loadarea container-0-0)
    (surface____ depot48-1-1)
    (storearea__ container-0-2)
    (available hoist2)
    (crate______ crate2)
    (connected depot48-2-3 depot48-2-2)
    (on crate0 container-0-0)
    (on crate2 container-0-2)
    (place______ container0)
    (surface____ depot48-1-3)
    (crate______ crate1)
    (clear depot48-1-4)
    (in crate3 container0)
    (surface____ depot48-1-4)
    (area_______ container-0-3)
    (surface____ crate2)
    (surface____ depot48-2-3)
    (place______ depot48)
    (connected depot48-2-2 depot48-2-1)
    (at hoist1 depot48-1-2)
    (area_______ container-0-1)
    (surface____ container-0-0)
    (area_______ depot48-1-1)
    (connected loadarea container-0-2)
    (storearea__ depot48-2-4)
    (connected depot48-1-2 depot48-1-1)
    (clear depot48-2-4)
    (in crate1 container0)
    (connected depot48-1-1 depot48-1-2)
    (connected depot48-1-2 depot48-1-3)
    (on crate1 container-0-1)
    (in crate0 container0)
    (area_______ depot48-1-3)
    (hoist______ hoist0)
    (area_______ container-0-2)
    (in depot48-1-4 depot48)
    (area_______ depot48-1-4)
    (surface____ crate0)
    (clear depot48-2-2)
    (surface____ depot48-2-2)
    (in container-0-3 container0)
    (area_______ depot48-2-3)
    (surface____ depot48-1-2)
    (storearea__ container-0-3)
    (surface____ container-0-2)
    (connected depot48-2-1 depot48-1-1)
    (storearea__ depot48-2-1)
    (in depot48-1-2 depot48)
    (depot______ depot48)
    (area_______ container-0-0)
    (connected depot48-1-3 depot48-2-3)
    (storearea__ container-0-1)
    (connected depot48-2-4 depot48-2-3)
    (injected---0)
  )
  (
    :goal
    (
      and
      (in crate0 depot48)
      (in crate1 depot48)
      (in crate2 depot48)
      (in crate3 depot48)
      (injected---0)
    )
  )
)