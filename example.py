"""Exemples d'utilisation du client COG (Code Officiel Géographique) INSEE."""

import asyncio
import logging

from cogpy import COG, COGException

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


async def async_main() -> None:
    """Exemples d'utilisation de l'API COG INSEE."""
    api = COG()

    try:
        # ── Commune ───────────────────────────────────────────────────────────
        # Récupérer une commune par son code INSEE
        paris = await api.async_get_commune("75056")
        logger.info("Commune Paris : %s", paris)

        # Chercher des communes par nom
        communes = await api.async_get_all_communes(filtre_nom="Bordeaux")
        logger.info("Communes 'Bordeaux' (%d) : %s", len(communes), communes)

        # Historique : commune à une date précise
        commune_1999 = await api.async_get_commune("75056", date="1999-01-01")
        logger.info("Paris en 1999 : %s", commune_1999)

        # Ascendants d'une commune (département, région…)
        ascendants = await api.async_get_commune_ascendants("75056")
        logger.info("Ascendants de Paris : %s", ascendants)

        # ── Département ───────────────────────────────────────────────────────
        dept = await api.async_get_departement("75")
        logger.info("Département 75 : %s", dept)

        deps = await api.async_get_all_departements()
        logger.info("Nombre de départements : %d", len(deps))

        communes_dept = await api.async_get_departement_descendants(
            "75", type="Commune"
        )
        logger.info("Communes du dép. 75 (%d)", len(communes_dept))

        # ── Région ────────────────────────────────────────────────────────────
        region = await api.async_get_region("11")
        logger.info("Région Île-de-France : %s", region)

        regions = await api.async_get_all_regions()
        logger.info("Nombre de régions : %d", len(regions))

        # ── EPCI ──────────────────────────────────────────────────────────────
        epci = await api.async_get_epci("200054781")
        logger.info("EPCI : %s", epci)

        # Communes membres de l'EPCI
        membres = await api.async_get_epci_descendants("200054781", type="Commune")
        logger.info("Communes membres (%d) : %s", len(membres), membres)

        # ── Canton ────────────────────────────────────────────────────────────
        canton = await api.async_get_canton("7417")
        logger.info("Canton 7417 : %s", canton)

        communes_canton = await api.async_get_canton_communes("7417")
        logger.info("Communes du canton 7417 (%d)", len(communes_canton))

        # ── Pays ──────────────────────────────────────────────────────────────
        france = await api.async_get_pays("99100")
        logger.info("France : %s", france)

        # Tous les pays
        pays = await api.async_get_all_pays()
        logger.info("Nombre de pays : %d", len(pays))

        # ── Arrondissements municipaux (Paris, Lyon, Marseille) ───────────────
        arr = await api.async_get_arrondissement_municipal("75101")
        logger.info("1er arrondissement de Paris : %s", arr)

        # ── Zone d'emploi ─────────────────────────────────────────────────────
        ze = await api.async_get_zone_emploi("2415")
        logger.info("Zone d'emploi 0051 : %s", ze)

        # ── Bassin de vie ─────────────────────────────────────────────────────
        bv = await api.async_get_bassin_vie("01004")
        logger.info("Bassin de vie 01004 : %s", bv)

        # ── Projection : à quoi ressemblera une commune à une date future ─────
        projetes = await api.async_get_commune_projetes(
            "24322", date_projection="2025-01-01"
        )
        logger.info("Commune 24322 projetée en 2025 : %s", projetes)

        # ── Tout l'historique avec date='*' ───────────────────────────────────
        historique = await api.async_get_commune_precedents("14475")
        logger.info("Historique Paris (%d entrées)", len(historique))

    except COGException as err:
        logger.error("Erreur COG : %s", err)

    finally:
        await api.async_close()


if __name__ == "__main__":
    asyncio.run(async_main())
