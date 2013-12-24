<%inherit file="base.mako"/>

<div class="container">
    <div class="row">
        <div class="col-md-2">
            <div class="bs-sidebar">
                <ul class="bs-sidenav nav">
                    <li><a href="#informations">Informations</a></li>
                    <li><a href="#abstract">Abstract</a></li>
                </ul>
            </div>
            <div><%block name="toco" /></div>
        </div>
        <div class="col-md-10">
            ${next.body()}
        </div>
    </div>
</div>
