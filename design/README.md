# Contratto dati proposto / Proposed data contract

IT: [adventure-authoring.schema.json](adventure-authoring.schema.json) sviluppa l'idea di separare descrizione pubblica e segreti del narratore emersa nella revisione Gemini indicata dal manutentore. È una **bozza di formato per l'autore**, non un'applicazione, un pacchetto giocatori o un meccanismo di autorizzazione. I campi obbligatori e i limiti dei valori sono espliciti; la sola validazione dello schema non verifica unicità degli ID, integrità dei collegamenti fra zone, raggiungibilità o correttezza dei contenuti pubblici.

Prima di un gioco remoto occorreranno: validazione semantica, scelta delle sole scene autorizzate e costruzione di un payload giocatori che ometta interamente `gm_secrets`. Anche `public_view` va controllato: etichettare un campo come pubblico non impedisce all'autore di inserirvi uno spoiler. Il file completo rimane un documento del narratore.

EN: [adventure-authoring.schema.json](adventure-authoring.schema.json) develops the public/facilitator separation suggested in the maintainer-supplied Gemini review. It is an **authoring-format draft**, not an application, player package or authorization mechanism. Required fields and value limits are explicit; schema validation alone does not verify unique IDs, valid zone references, reachability or safe public content.

Remote play will require semantic validation, authorized-scene selection and a player payload that omits `gm_secrets` completely. Authors must also review `public_view`: a label cannot prevent spoilers being placed there. The full file remains a facilitator document.

Licenza / License: CC BY-SA 4.0 as a design document. No third-party game text or assets included.
