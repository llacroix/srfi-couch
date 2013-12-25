<%inherit file="../base.mako"/>

<%def name="jumbotron(title, text)">
<div class="jumbotron">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h1>${title}</h1>
                <p>${text|n}</p>
            </div>
        </div>
    </div>
</div>
</%def>

<%def name="render_column(column)">
    <div class="col-md-${column.get('size')}">
        % for col in column.get("@content"):
            ${render_content(col)}
        % endfor
    </div>
</%def>

<%def name="render_container(container)">
    <div class="container">
        <div class="row">
        % for col in container.get("@content"):
            ${render_column(col)}
        % endfor
        </div>
    </div>
</%def>

<%def name="render_list(lst)">
    <h4>${lst.get("title")}</h4>
    <ul>
      % for elem in lst.get("@content"):
        <li>${render_content(elem)}</li>
      % endfor
    </ul>
</%def>

<%def name="render_link(lnk)">
<a href="${lnk.get('url')}">${lnk.get("text")}</a>
</%def>

<%def name="render_content(obj)">
    % if isinstance(obj, basestring):
        <p>
        ${obj}
        </p>
    % elif obj.get('type') == "jumbotron":
        ${jumbotron(obj.get("title"), obj.get("text"))}
    % elif obj.get('type') == "container":
        ${render_container(obj)}
    % elif obj.get('type') == "list":
        ${render_list(obj)}
    % elif obj.get('type') == "link":
        ${render_link(obj)}
    % else:
        ${obj}
    % endif
</%def>

<%def name="render_contents(elements)">
    % for elem in elements.get("@content"):
        ${render_content(elem)}
    % endfor
</%def>

${render_contents(ctx)}
