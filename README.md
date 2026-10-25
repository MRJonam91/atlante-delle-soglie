# Atlante delle Soglie · Atlas of Thresholds

**Un GDR fiabesco aperto per amici, famiglie ed esploratori di mondi.**

**An open fairy-tale tabletop RPG for friends, families and world explorers.**

Versione / Version **0.1.0-playtest** · Italiano / English · 1 narratore / facilitator + 3–5 giocatori / players.

## Italiano

Ogni mappa della Biblioteca delle Soglie conduce a un luogo che può ancora cambiare. I Custodi attraversano città impossibili, incontrano abitanti con desideri contrastanti e scelgono quali promesse portare con sé.

Questa edizione pubblica contiene **ambientazione e personaggi originali**, regole sperimentali, sei personaggi pronti e un'avventura completa per una prima prova. La complessità base è accessibile; dilemmi e conseguenze possono interessare anche giocatori esperti. Non sono ancora stati svolti playtest con gruppi reali.

### Cominciare a giocare

1. Leggi le [regole](docs/it/regole.md); il narratore legge anche [La Fiera dei Domani](docs/it/avventura.md).
2. Scegliete 3–5 dei [sei Custodi](docs/it/personaggi.md).
3. Aprite o stampate il [tabellone](print/board.svg) e le [pedine e i contatori](print/tokens.svg). Le mappe non riportano segreti; il testo dell'avventura sì.
4. Procuratevi almeno un d20 e carta; per l'officina è utile un d6. Monete o bottoni possono sostituire le pedine.
5. Usate la [scheda di sessione e il questionario](docs/it/playtest.md). La durata indicativa di 90–150 minuti è un obiettivo da verificare.

Nessun account, acquisto, mazzo commerciale, soundtrack o servizio online è necessario. Tutto il materiale di gioco è consultabile nei file della repository. Le due SVG sono pensate per A4 orizzontale, con stampa adattata alla pagina.

### Creare e sviluppare

L'[officina e atlante](docs/it/officina.md) contiene sei mondi autonomi e un metodo per creare avventure. La [roadmap](docs/ROADMAP.md) descrive il futuro tavolo digitale: mappe, dadi, segreti del narratore, effetti e salvataggi. **L'applicazione non è ancora implementata.**

### Licenze e attribuzione

Manuali, avventure, personaggi, mappe e pedine originali: **[CC BY-SA 4.0](LICENSE)**. Potete copiarli, modificarli e venderli rispettando attribuzione, indicazione delle modifiche e ShareAlike. Gli strumenti in `tools/` e le automazioni sono **[GPL-3.0-or-later](LICENSES/GPL-3.0-or-later.txt)**; ambiti dettagliati in [LICENSING.md](LICENSING.md).

Attribuzione suggerita: «Basato su *Atlante delle Soglie* di MRJonam91 e contributori, CC BY-SA 4.0, https://github.com/MRJonam91/atlante-delle-soglie. Modifiche: …». È un esempio, non un obbligo di usare una formula identica. Conservate gli avvisi applicabili.

I nomi di terzi nelle sole note di ricerca non indicano affiliazione o approvazione. La licenza copre i contributi licenziabili del progetto; non concede marchi, personaggi, immagini o musica altrui. Nessun materiale di franchise è incluso come contenuto giocabile. Vedi [diritti e possibilità commerciali](docs/RIGHTS_AND_COMMERCIAL.md) e [provenienza](ASSETS.md).

### Contribuire, assistenza e sicurezza

Leggi [CONTRIBUTING](CONTRIBUTING.md), [codice di condotta](CODE_OF_CONDUCT.md), [assistenza](SUPPORT.md) e [sicurezza](SECURITY.md). Le versioni attualmente compatibili sono i file di questa edizione: non è dichiarata compatibilità con altri regolamenti o giochi di carte. Il [changelog](CHANGELOG.md) distingue quanto disponibile da quanto pianificato.

### Sostieni il progetto

Il sostegno è volontario: [GitHub Sponsors](https://github.com/sponsors/MRJonam91), [Ko-fi](https://ko-fi.com/mrjonam), [Buy Me a Coffee](https://buymeacoffee.com/mrjonam) o [PayPal](https://paypal.me/manorollo). Non attribuisce diritti aggiuntivi e sostiene soltanto il progetto originale indipendente.

## English

Every map in the Library of Thresholds leads somewhere that can still change. Keepers explore impossible cities, meet people with conflicting wishes and decide which promises to carry forward.

This public edition provides an **original setting and characters**, experimental rules, six ready-made Keepers and one complete introductory adventure. The base rules support mixed groups; dilemmas and consequences also offer material for experienced players. No sessions with real playtest groups have been completed yet.

### Start playing

1. Read the [rules](docs/en/rules.md); the facilitator also reads [The Fair of Tomorrows](docs/en/adventure.md).
2. Choose 3–5 of the [six Keepers](docs/en/characters.md).
3. Open or print the [board](print/board.svg) and [tokens and trackers](print/tokens.svg). The maps contain no secrets; the adventure text does.
4. Bring at least one d20 and paper; a d6 helps with the workshop. Coins or buttons can replace tokens.
5. Use the [session record and feedback form](docs/en/playtest.md). The proposed 90–150 minute duration still needs testing.

No account, purchase, commercial card deck, soundtrack or online service is required. Both SVGs are designed for landscape A4, printed with fit-to-page enabled.

The [workshop and atlas](docs/en/workshop.md) provides six independent worlds and an adventure-building method. The [roadmap](docs/ROADMAP.md) describes a future digital table with maps, dice, facilitator secrets, effects and saves. **That application has not been implemented.**

Original game content and printable artwork use **CC BY-SA 4.0**; tools and automation use **GPL-3.0-or-later**. Copying, adaptation and commercial reuse are allowed subject to the applicable license. See [LICENSING.md](LICENSING.md) and [NOTICE](NOTICE).

Suggested credit: “Based on *Atlas of Thresholds / Atlante delle Soglie* by MRJonam91 and contributors, CC BY-SA 4.0, https://github.com/MRJonam91/atlante-delle-soglie. Changes: …”. Equivalent reasonable attribution is welcome. Third-party rights and trademarks are not licensed by this project; no franchise material is distributed as playable content.

Read the [contribution guide](CONTRIBUTING.md), [conduct policy](CODE_OF_CONDUCT.md), [support](SUPPORT.md), [security policy](SECURITY.md), [rights review](docs/RIGHTS_AND_COMMERCIAL.md) and [changelog](CHANGELOG.md). No compatibility with other RPG systems or trading-card games is claimed.

### Support the project

Optional support: [GitHub Sponsors](https://github.com/sponsors/MRJonam91), [Ko-fi](https://ko-fi.com/mrjonam), [Buy Me a Coffee](https://buymeacoffee.com/mrjonam), [PayPal](https://paypal.me/manorollo). Donations support this independent original project and confer no additional rights.

## Repository checks / Controlli

Python 3.11+ is needed only for maintainer checks, not for play:

```sh
python tools/check_publication.py
```

The check verifies local document links, the expected publication files, SVG safety and restricted-content patterns. It is not a legal opinion or proof of game balance.
