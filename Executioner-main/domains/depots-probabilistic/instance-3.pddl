(
  define
  (problem instance-3)
  (:domain depots)
  (:objects truck2 depot1 depot0 truck1 hoist1 hoist5 truck4 hoist4 distributor2 distributor3 distributor1 pallet0 truck0 distributor0 hoist2 crate3 pallet4 pallet1 crate2 crate0 pallet5 pallet3 truck3 hoist3 crate1 pallet2 hoist0)
  (
    :init
    (at truck2 distributor2)
    (crate_____ crate0)
    (at truck0 depot0)
    (pallet____ pallet3)
    (available hoist1)
    (locatable_ truck2)
    (at crate0 depot1)
    (clear pallet4)
    (on crate2 pallet5)
    (at pallet1 depot1)
    (surface___ crate2)
    (pallet____ pallet2)
    (at pallet2 distributor0)
    (hoist_____ hoist2)
    (surface___ crate1)
    (at pallet4 distributor2)
    (locatable_ pallet3)
    (truck_____ truck4)
    (place_____ depot0)
    (distributor distributor0)
    (locatable_ pallet2)
    (place_____ distributor0)
    (clear crate2)
    (at hoist5 distributor3)
    (pallet____ pallet0)
    (crate_____ crate3)
    (pallet____ pallet1)
    (surface___ pallet0)
    (surface___ crate0)
    (place_____ depot1)
    (locatable_ pallet0)
    (locatable_ pallet1)
    (available hoist0)
    (at truck1 distributor0)
    (locatable_ crate0)
    (distributor distributor1)
    (at hoist1 depot1)
    (on crate3 crate1)
    (clear crate0)
    (at crate1 depot0)
    (at hoist0 depot0)
    (available hoist4)
    (locatable_ truck0)
    (locatable_ hoist3)
    (locatable_ truck1)
    (truck_____ truck1)
    (distributor distributor2)
    (distributor distributor3)
    (truck_____ truck3)
    (locatable_ pallet5)
    (at hoist2 distributor0)
    (locatable_ hoist1)
    (at pallet5 distributor3)
    (surface___ crate3)
    (at hoist4 distributor2)
    (available hoist3)
    (surface___ pallet3)
    (available hoist2)
    (locatable_ crate3)
    (at crate3 depot0)
    (locatable_ pallet4)
    (hoist_____ hoist3)
    (on crate0 pallet1)
    (surface___ pallet2)
    (truck_____ truck2)
    (locatable_ truck4)
    (depot_____ depot1)
    (clear crate3)
    (hoist_____ hoist1)
    (at crate2 distributor3)
    (clear pallet3)
    (at truck3 depot0)
    (locatable_ crate2)
    (clear pallet2)
    (locatable_ crate1)
    (at truck4 depot1)
    (surface___ pallet1)
    (locatable_ hoist0)
    (crate_____ crate2)
    (crate_____ crate1)
    (locatable_ hoist4)
    (place_____ distributor1)
    (on crate1 pallet0)
    (pallet____ pallet5)
    (hoist_____ hoist0)
    (locatable_ hoist5)
    (surface___ pallet5)
    (locatable_ truck3)
    (place_____ distributor2)
    (pallet____ pallet4)
    (place_____ distributor3)
    (hoist_____ hoist4)
    (at pallet3 distributor1)
    (depot_____ depot0)
    (truck_____ truck0)
    (at pallet0 depot0)
    (surface___ pallet4)
    (available hoist5)
    (locatable_ hoist2)
    (hoist_____ hoist5)
    (at hoist3 distributor1)
    (injected---0)
  )
  (
    :goal
    (
      and
      (on crate1 crate2)
      (on crate2 pallet2)
      (on crate3 pallet4)
      (injected---0)
    )
  )
)