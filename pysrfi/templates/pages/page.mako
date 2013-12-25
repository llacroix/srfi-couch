<%inherit file="../base.mako"/>

<%block name="title">
    Current user is ${current_user}
</%block>

${self.render_contents(ctx)}
