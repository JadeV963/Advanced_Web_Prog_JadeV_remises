## Debugging Report
## Bug 1: SQLAlchemy never inizialized with the app

**App.py**

## db = SQLAlchemy was assignging the SQLAlchemy class itself to  db, instead of creating an instance connected to the Flask app. This meant db had no link to the app's configuration, nothing database-related could work.

## I changed it to db = SQLAlchemy(app), calling SQLAlchemy as a constructor with the app passed in.

## Ran python3 app.py in terminal. Before the fix, Flask would not start correctly. After fixing, combined with the other Stage 1 corrections, the app started without a traceback.

---

## Bug 2: add_album route only accepted GET requests

**File**
**app.py**

## The route was defined as methods=["GET"], but the function body contained an if request.method == "POST": block meant to handle form submissions. PoST was never allowed, so that block could not run.

## I changed the route to methods=["GET", "POST"], so the ofrm submission could actually be processed.

## I filled hte Add Album form and clicked "Save Album." Before the fix, nothing happened. After the fix, the album was created and the page redirected to the album list.


## Bug 3: Missing `db.session.commit()` in edit_album

**File app.py**

## the edit_album function updated the album's attribute (album.title, album.artist, etc.) but never called db.session.commit(). Without a commit, changes only exist in memory and are never written to the database.

## I added `db.session.commit()`right after updating all the album's fields, before the redirect.

## Edited an album's title and clicked "Update album". Before the fix, the change did not persist ( it reverted after restarting Flask or reloading the page). After the fix, the update title appeared in the album list and stayed after restarting Flask.

## Bug 4: Template used wrong attribute names

**Files**

## templatess/index.html ##

## The album card used item name and item.band, but the album model only had title and artist coulms. Since name and band don't exist on the model, Jinja rendered then as empty instead of raisinf an error.

## I changed the template to usa item.title and item artist, matching the actual model attributes.

## Reloaded the album lis page. Before the fix, every album card showed a blank itlte and a blank artist. After the fix, both fields diplayed correctly.





