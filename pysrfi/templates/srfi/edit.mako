<%inherit file="page-base.mako"/>

<form role="form" action="${ctx.url("@@edit")}" method="post">
  <input type="hidden" name="_id" value="${ctx.get("_id")}" />
  <input type="hidden" name="_rev" value="${ctx.get("_rev")}" />

  <div class="form-group">
    <label for="exampleInputEmail1">Srfi-code:</label>
    <input type="text" class="form-control" placeholder="#number" value="${ctx.get("srfi-code") or ""}" />
  </div>

  <div class="form-group">
    <label for="exampleInputEmail1">Status:</label>
    <select name="status">
        <option>active</option>
        <option>final</option>
        <option>withdrawn</option>
    </select>
  </div>

  <div class="form-group">
    <label for="exampleInputEmail1">Title:</label>
    <input type="text" class="form-control" name="title" placeholder="" value="${ctx.get("title")}" />
  </div>

  <div class="form-group">
    <label for="exampleInputEmail1">Author:</label>
    <input type="text" class="form-control" name="author" placeholder="" value="${ctx.get("author")}" />
  </div>

  <div class="form-group">
    <label for="exampleInputEmail1">Content:</label>
    <textarea class="form-control content-editor" name="content" placeholder="">${ctx.get("content")}</textarea>
  </div>

  <div class="form-group">
    <label for="exampleInputFile">Implementation</label>
    <input type="file" id="exampleInputFile">
    <p class="help-block">Download an implementation file.</p>
  </div>

  <button type="submit" class="btn btn-default">Submit</button>
</form>
