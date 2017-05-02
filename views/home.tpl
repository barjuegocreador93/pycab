%rebase(template('index'))
<header class="row panel">
   <ul class="nav nav-tabs">
      <li role="presentation" class="active"><a>PyCab</a></li>
      <li role='presentation' class=""><a class="" href="https://github.com/barjuegocreador93/pycab#pycab">Documentation</a></li>
      <li role="presentation"> <a role='button' class="" href="http://getbootstrap.com/css/">Bootstarp</a></li>

   </ul>

   <div class="col-sm-12">ss

      <h1 class="text-center">{{APP_NAME}}</h1>

      <p class="lead text-center">Make something great!!</p>
       <div class="row container">
          <div class="col-sm-4"></div>
         <div class=" panel panel-primary col-sm-4">
            <div class="panel-heading">
               Inlcudes:
            </div>
            <div class="panel-body">
               <ul class="list-group">
               %for i in mylist:
                  <li class="list-group-item leader text-center">{{i.capitalize()}}</li>
               %end
               </ul>
            </div>


         </div>
       </div>
   </div>
</header>

%include(template('scripts'))