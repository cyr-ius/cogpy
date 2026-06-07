"""COG API client for querying INSEE geographical data."""

import logging
from typing import Any

from .auth import HTTPRequest
from .consts import API_BASE_URL_COG

_LOGGER = logging.getLogger(__name__)


class COG(HTTPRequest):
    """Client pour l'API COG (Code Officiel Géographique) de l'INSEE."""

    async def _geo(self, path: str, params: dict[str, Any] | None = None) -> Any:
        """Appel générique vers un endpoint géographique."""
        url = f"{API_BASE_URL_COG}/{path}"
        filtered = {k: v for k, v in (params or {}).items() if v is not None}
        return await self.async_request(
            url,
            params=filtered if filtered else None,
            headers={"Accept": "application/json"},
        )

    # ──────────────────────────── Pays ────────────────────────────

    async def async_get_pays(self, code: str, date: str | None = None) -> dict:
        """Retourne le pays identifié par son code (5 chiffres commençant par 99)."""
        return await self._geo(f"pays/{code}", {"date": date})

    async def async_get_all_pays(
        self, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne la liste de tous les pays."""
        return await self._geo("pays", {"date": date, "type": type})

    async def async_get_pays_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les territoires descendants du pays."""
        return await self._geo(f"pays/{code}/descendants", {"date": date, "type": type})

    async def async_get_pays_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les pays prédécesseurs."""
        return await self._geo(f"pays/{code}/precedents", {"date": date})

    async def async_get_pays_suivants(self, code: str, date: str | None = None) -> list:
        """Retourne les pays successeurs."""
        return await self._geo(f"pays/{code}/suivants", {"date": date})

    # ──────────────────────── Région ──────────────────────────────

    async def async_get_region(self, code: str, date: str | None = None) -> dict:
        """Retourne la région identifiée par son code (2 chiffres)."""
        return await self._geo(f"region/{code}", {"date": date})

    async def async_get_all_regions(self, date: str | None = None) -> list:
        """Retourne la liste de toutes les régions."""
        return await self._geo("regions", {"date": date})

    async def async_get_region_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de la région."""
        return await self._geo(
            f"region/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_region_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de la région."""
        return await self._geo(
            f"region/{code}/descendants", {"date": date, "type": type}
        )

    async def async_get_region_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les régions prédécesseures."""
        return await self._geo(f"region/{code}/precedents", {"date": date})

    async def async_get_region_projetes(self, code: str, date_projection: str) -> list:
        """Retourne les régions projetées à une date donnée."""
        return await self._geo(
            f"region/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_region_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les régions successeures."""
        return await self._geo(f"region/{code}/suivants", {"date": date})

    # ──────────────────────── Département ─────────────────────────

    async def async_get_departement(self, code: str, date: str | None = None) -> dict:
        """Retourne le département identifié par son code."""
        return await self._geo(f"departement/{code}", {"date": date})

    async def async_get_all_departements(self, date: str | None = None) -> list:
        """Retourne la liste de tous les départements."""
        return await self._geo("departements", {"date": date})

    async def async_get_departement_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes du département."""
        return await self._geo(
            f"departement/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_departement_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes du département."""
        return await self._geo(
            f"departement/{code}/descendants", {"date": date, "type": type}
        )

    async def async_get_departement_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les départements prédécesseurs."""
        return await self._geo(f"departement/{code}/precedents", {"date": date})

    async def async_get_departement_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les départements projetés à une date donnée."""
        return await self._geo(
            f"departement/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_departement_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les départements successeurs."""
        return await self._geo(f"departement/{code}/suivants", {"date": date})

    # ──────────────────────── Commune ─────────────────────────────

    async def async_get_commune(self, code: str, date: str | None = None) -> dict:
        """Retourne la commune identifiée par son code INSEE (5 caractères)."""
        return await self._geo(f"commune/{code}", {"date": date})

    async def async_get_all_communes(
        self,
        date: str | None = None,
        type: str | None = None,
        filtre_nom: str | None = None,
    ) -> list:
        """Retourne la liste de toutes les communes."""
        return await self._geo(
            "communes", {"date": date, "type": type, "filtreNom": filtre_nom}
        )

    async def async_get_commune_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de la commune."""
        return await self._geo(
            f"commune/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_commune_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de la commune."""
        return await self._geo(
            f"commune/{code}/descendants", {"date": date, "type": type}
        )

    async def async_get_commune_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les communes prédécesseures."""
        return await self._geo(f"commune/{code}/precedents", {"date": date})

    async def async_get_commune_projetes(self, code: str, date_projection: str) -> list:
        """Retourne les communes projetées à une date donnée."""
        return await self._geo(
            f"commune/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_commune_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les communes successeures."""
        return await self._geo(f"commune/{code}/suivants", {"date": date})

    # ──────────────────── Commune Associée ────────────────────────

    async def async_get_commune_associee(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne la commune associée identifiée par son code."""
        return await self._geo(f"communeAssociee/{code}", {"date": date})

    async def async_get_all_communes_associees(
        self, date: str | None = None, filtre_nom: str | None = None
    ) -> list:
        """Retourne la liste de toutes les communes associées."""
        return await self._geo(
            "communesAssociees", {"date": date, "filtreNom": filtre_nom}
        )

    async def async_get_commune_associee_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de la commune associée."""
        return await self._geo(
            f"communeAssociee/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_commune_associee_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les communes associées prédécesseures."""
        return await self._geo(f"communeAssociee/{code}/precedents", {"date": date})

    async def async_get_commune_associee_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les communes associées projetées."""
        return await self._geo(
            f"communeAssociee/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_commune_associee_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les communes associées successeures."""
        return await self._geo(f"communeAssociee/{code}/suivants", {"date": date})

    # ──────────────────── Commune Déléguée ────────────────────────

    async def async_get_commune_deleguee(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne la commune déléguée identifiée par son code."""
        return await self._geo(f"communeDeleguee/{code}", {"date": date})

    async def async_get_all_communes_deleguees(
        self, date: str | None = None, filtre_nom: str | None = None
    ) -> list:
        """Retourne la liste de toutes les communes déléguées."""
        return await self._geo(
            "communesDeleguees", {"date": date, "filtreNom": filtre_nom}
        )

    async def async_get_commune_deleguee_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de la commune déléguée."""
        return await self._geo(
            f"communeDeleguee/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_commune_deleguee_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les communes déléguées prédécesseures."""
        return await self._geo(f"communeDeleguee/{code}/precedents", {"date": date})

    async def async_get_commune_deleguee_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les communes déléguées projetées."""
        return await self._geo(
            f"communeDeleguee/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_commune_deleguee_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les communes déléguées successeures."""
        return await self._geo(f"communeDeleguee/{code}/suivants", {"date": date})

    # ──────────────────────── EPCI ────────────────────────────────

    async def async_get_epci(self, code: str, date: str | None = None) -> dict:
        """Retourne l'intercommunalité (EPCI) identifiée par son code SIREN."""
        return await self._geo(f"intercommunalite/{code}", {"date": date})

    async def async_get_all_epcis(self, date: str | None = None) -> list:
        """Retourne la liste de toutes les intercommunalités (EPCI)."""
        return await self._geo("intercommunalites", {"date": date})

    async def async_get_epci_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de l'intercommunalité."""
        return await self._geo(
            f"intercommunalite/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_epci_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de l'intercommunalité."""
        return await self._geo(
            f"intercommunalite/{code}/descendants", {"date": date, "type": type}
        )

    async def async_get_epci_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les intercommunalités prédécesseures."""
        return await self._geo(f"intercommunalite/{code}/precedents", {"date": date})

    async def async_get_epci_projetes(self, code: str, date_projection: str) -> list:
        """Retourne les intercommunalités projetées à une date donnée."""
        return await self._geo(
            f"intercommunalite/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_epci_suivants(self, code: str, date: str | None = None) -> list:
        """Retourne les intercommunalités successeures."""
        return await self._geo(f"intercommunalite/{code}/suivants", {"date": date})

    # ──────────────────────── Arrondissements ─────────────────────

    async def async_get_arrondissement(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne l'arrondissement identifié par son code (3-4 caractères)."""
        return await self._geo(f"arrondissement/{code}", {"date": date})

    async def async_get_all_arrondissements(self, date: str | None = None) -> list:
        """Retourne la liste de tous les arrondissements."""
        return await self._geo("arrondissements", {"date": date})

    async def async_get_arrondissement_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de l'arrondissement."""
        return await self._geo(
            f"arrondissement/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_arrondissement_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de l'arrondissement."""
        return await self._geo(
            f"arrondissement/{code}/descendants", {"date": date, "type": type}
        )

    async def async_get_arrondissement_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les arrondissements prédécesseurs."""
        return await self._geo(f"arrondissement/{code}/precedents", {"date": date})

    async def async_get_arrondissement_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les arrondissements projetés à une date donnée."""
        return await self._geo(
            f"arrondissement/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_arrondissement_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les arrondissements successeurs."""
        return await self._geo(f"arrondissement/{code}/suivants", {"date": date})

    # ─────────────────── Arrondissements Municipaux ───────────────

    async def async_get_arrondissement_municipal(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne l'arrondissement municipal identifié par son code (5 caractères)."""
        return await self._geo(f"arrondissementMunicipal/{code}", {"date": date})

    async def async_get_all_arrondissements_municipaux(
        self, date: str | None = None
    ) -> list:
        """Retourne la liste de tous les arrondissements municipaux."""
        return await self._geo("arrondissementsMunicipaux", {"date": date})

    async def async_get_arrondissement_municipal_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de l'arrondissement municipal."""
        return await self._geo(
            f"arrondissementMunicipal/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_arrondissement_municipal_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les arrondissements municipaux prédécesseurs."""
        return await self._geo(
            f"arrondissementMunicipal/{code}/precedents", {"date": date}
        )

    async def async_get_arrondissement_municipal_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les arrondissements municipaux projetés."""
        return await self._geo(
            f"arrondissementMunicipal/{code}/projetes",
            {"dateProjection": date_projection},
        )

    async def async_get_arrondissement_municipal_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les arrondissements municipaux successeurs."""
        return await self._geo(
            f"arrondissementMunicipal/{code}/suivants", {"date": date}
        )

    # ──────────────────────────── Cantons ─────────────────────────

    async def async_get_canton(self, code: str, date: str | None = None) -> dict:
        """Retourne le canton identifié par son code (4 chiffres métro, 5 DOM)."""
        return await self._geo(f"canton/{code}", {"date": date})

    async def async_get_all_cantons(self, date: str | None = None) -> list:
        """Retourne la liste de tous les cantons."""
        return await self._geo("cantons", {"date": date})

    async def async_get_canton_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes du canton."""
        return await self._geo(
            f"canton/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_canton_communes(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les communes dont le territoire est inclus dans le canton."""
        return await self._geo(f"canton/{code}/communes", {"date": date})

    async def async_get_canton_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les cantons prédécesseurs."""
        return await self._geo(f"canton/{code}/precedents", {"date": date})

    async def async_get_canton_projetes(self, code: str, date_projection: str) -> list:
        """Retourne les cantons projetés à une date donnée."""
        return await self._geo(
            f"canton/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_canton_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les cantons successeurs."""
        return await self._geo(f"canton/{code}/suivants", {"date": date})

    # ──────────────────────── Canton ou Ville ─────────────────────

    async def async_get_canton_ou_ville(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne le canton-ou-ville identifié par son code."""
        return await self._geo(f"cantonOuVille/{code}", {"date": date})

    async def async_get_all_cantons_et_villes(self, date: str | None = None) -> list:
        """Retourne la liste de tous les cantons-et-villes."""
        return await self._geo("cantonsEtVilles", {"date": date})

    async def async_get_canton_ou_ville_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes du canton-ou-ville."""
        return await self._geo(
            f"cantonOuVille/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_canton_ou_ville_descendants(
        self,
        code: str,
        date: str | None = None,
        type: str | None = None,
        filtre_nom: str | None = None,
    ) -> list:
        """Retourne les entités descendantes du canton-ou-ville."""
        return await self._geo(
            f"cantonOuVille/{code}/descendants",
            {"date": date, "type": type, "filtreNom": filtre_nom},
        )

    async def async_get_canton_ou_ville_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les cantons-ou-villes prédécesseurs."""
        return await self._geo(f"cantonOuVille/{code}/precedents", {"date": date})

    async def async_get_canton_ou_ville_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les cantons-ou-villes projetés."""
        return await self._geo(
            f"cantonOuVille/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_canton_ou_ville_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les cantons-ou-villes successeurs."""
        return await self._geo(f"cantonOuVille/{code}/suivants", {"date": date})

    # ──────────────── Aire d'Attraction des Villes 2020 ───────────

    async def async_get_aire_attraction_villes(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne l'aire d'attraction des villes identifiée par son code (3 caractères)."""
        return await self._geo(f"aireDAttractionDesVilles2020/{code}", {"date": date})

    async def async_get_all_aires_attraction_villes(
        self, date: str | None = None
    ) -> list:
        """Retourne la liste de toutes les aires d'attraction des villes 2020."""
        return await self._geo("airesDAttractionDesVilles2020", {"date": date})

    async def async_get_aire_attraction_villes_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de l'aire d'attraction des villes."""
        return await self._geo(
            f"aireDAttractionDesVilles2020/{code}/descendants",
            {"date": date, "type": type},
        )

    # ─────────────────────── Bassin de Vie 2022 ───────────────────

    async def async_get_bassin_vie(self, code: str, date: str | None = None) -> dict:
        """Retourne le bassin de vie 2022 identifié par son code (5 caractères)."""
        return await self._geo(f"bassinDeVie2022/{code}", {"date": date})

    async def async_get_all_bassins_vie(
        self, date: str | None = None, filtre_nom: str | None = None
    ) -> list:
        """Retourne la liste de tous les bassins de vie 2022."""
        return await self._geo(
            "bassinsDeVie2022", {"date": date, "filtreNom": filtre_nom}
        )

    async def async_get_bassin_vie_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes du bassin de vie."""
        return await self._geo(
            f"bassinDeVie2022/{code}/descendants", {"date": date, "type": type}
        )

    # ─────────────── Circonscription Territoriale ─────────────────

    async def async_get_circonscription_territoriale(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne la circonscription territoriale identifiée par son code (5 caractères)."""
        return await self._geo(f"circonscriptionTerritoriale/{code}", {"date": date})

    async def async_get_all_circonscriptions_territoriales(
        self, date: str | None = None
    ) -> list:
        """Retourne la liste de toutes les circonscriptions territoriales."""
        return await self._geo("circonscriptionsTerritoriales", {"date": date})

    async def async_get_circonscription_territoriale_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de la circonscription territoriale."""
        return await self._geo(
            f"circonscriptionTerritoriale/{code}/ascendants",
            {"date": date, "type": type},
        )

    async def async_get_circonscription_territoriale_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de la circonscription territoriale."""
        return await self._geo(
            f"circonscriptionTerritoriale/{code}/descendants",
            {"date": date, "type": type},
        )

    async def async_get_circonscription_territoriale_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les circonscriptions territoriales prédécesseures."""
        return await self._geo(
            f"circonscriptionTerritoriale/{code}/precedents", {"date": date}
        )

    async def async_get_circonscription_territoriale_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les circonscriptions territoriales projetées."""
        return await self._geo(
            f"circonscriptionTerritoriale/{code}/projetes",
            {"dateProjection": date_projection},
        )

    async def async_get_circonscription_territoriale_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les circonscriptions territoriales successeures."""
        return await self._geo(
            f"circonscriptionTerritoriale/{code}/suivants", {"date": date}
        )

    # ──────────────── Collectivité d'Outre-Mer ────────────────────

    async def async_get_collectivite_outre_mer(
        self, code: str, date: str | None = None
    ) -> dict:
        """Retourne la collectivité d'outre-mer identifiée par son code."""
        return await self._geo(f"collectiviteDOutreMer/{code}", {"date": date})

    async def async_get_all_collectivites_outre_mer(
        self, date: str | None = None
    ) -> list:
        """Retourne la liste de toutes les collectivités d'outre-mer."""
        return await self._geo("collectivitesDOutreMer", {"date": date})

    async def async_get_collectivite_outre_mer_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes de la collectivité d'outre-mer."""
        return await self._geo(
            f"collectiviteDOutreMer/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_collectivite_outre_mer_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de la collectivité d'outre-mer."""
        return await self._geo(
            f"collectiviteDOutreMer/{code}/descendants", {"date": date, "type": type}
        )

    async def async_get_collectivite_outre_mer_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les collectivités d'outre-mer prédécesseures."""
        return await self._geo(
            f"collectiviteDOutreMer/{code}/precedents", {"date": date}
        )

    async def async_get_collectivite_outre_mer_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les collectivités d'outre-mer projetées."""
        return await self._geo(
            f"collectiviteDOutreMer/{code}/projetes",
            {"dateProjection": date_projection},
        )

    async def async_get_collectivite_outre_mer_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les collectivités d'outre-mer successeures."""
        return await self._geo(f"collectiviteDOutreMer/{code}/suivants", {"date": date})

    # ──────────────────────── District ────────────────────────────

    async def async_get_district(self, code: str, date: str | None = None) -> dict:
        """Retourne le district identifié par son code."""
        return await self._geo(f"district/{code}", {"date": date})

    async def async_get_all_districts(self, date: str | None = None) -> list:
        """Retourne la liste de tous les districts."""
        return await self._geo("districts", {"date": date})

    async def async_get_district_ascendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités ascendantes du district."""
        return await self._geo(
            f"district/{code}/ascendants", {"date": date, "type": type}
        )

    async def async_get_district_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes du district."""
        return await self._geo(
            f"district/{code}/descendants", {"date": date, "type": type}
        )

    async def async_get_district_precedents(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les districts prédécesseurs."""
        return await self._geo(f"district/{code}/precedents", {"date": date})

    async def async_get_district_projetes(
        self, code: str, date_projection: str
    ) -> list:
        """Retourne les districts projetés."""
        return await self._geo(
            f"district/{code}/projetes", {"dateProjection": date_projection}
        )

    async def async_get_district_suivants(
        self, code: str, date: str | None = None
    ) -> list:
        """Retourne les districts successeurs."""
        return await self._geo(f"district/{code}/suivants", {"date": date})

    # ──────────────────── Unité Urbaine 2020 ──────────────────────

    async def async_get_unite_urbaine(self, code: str, date: str | None = None) -> dict:
        """Retourne l'unité urbaine 2020 identifiée par son code."""
        return await self._geo(f"uniteUrbaine2020/{code}", {"date": date})

    async def async_get_all_unites_urbaines(
        self, date: str | None = None, filtre_nom: str | None = None
    ) -> list:
        """Retourne la liste de toutes les unités urbaines 2020."""
        return await self._geo(
            "unitesUrbaines2020", {"date": date, "filtreNom": filtre_nom}
        )

    async def async_get_unite_urbaine_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de l'unité urbaine."""
        return await self._geo(
            f"uniteUrbaine2020/{code}/descendants", {"date": date, "type": type}
        )

    # ─────────────────── Zone d'Emploi 2020 ───────────────────────

    async def async_get_zone_emploi(self, code: str, date: str | None = None) -> dict:
        """Retourne la zone d'emploi 2020 identifiée par son code."""
        return await self._geo(f"zoneDEmploi2020/{code}", {"date": date})

    async def async_get_all_zones_emploi(
        self, date: str | None = None, filtre_nom: str | None = None
    ) -> list:
        """Retourne la liste de toutes les zones d'emploi 2020."""
        return await self._geo(
            "zonesEmploi2020", {"date": date, "filtreNom": filtre_nom}
        )

    async def async_get_zone_emploi_descendants(
        self, code: str, date: str | None = None, type: str | None = None
    ) -> list:
        """Retourne les entités descendantes de la zone d'emploi."""
        return await self._geo(
            f"zoneDEmploi2020/{code}/descendants", {"date": date, "type": type}
        )
