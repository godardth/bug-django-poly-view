# bug-django-poly-view
Reproduction of an issue with Django polymorphic MPTT.  
https://github.com/django-polymorphic/django-polymorphic/issues/383

## Issue with
```
Django==1.11.13
django-polymorphic==2.0.3
djangorestframework==3.9.3
```

## Summary
Django fails creating the first migrations when using polymorphic and Django Rest Framework simultaneously. The part of the code that triggers the error is the queryset in that part of the code :
```
class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
```

## Workaround
Commenting the viewset / reference to the viewset in the urls.py to make the first migration.

## Error Log
```
$ ./manage.py makemigrations
Traceback (most recent call last):
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.OperationalError: no such table: django_content_type

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "./manage.py", line 22, in <module>
    execute_from_command_line(sys.argv)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/management/__init__.py", line 364, in execute_from_command_line
    utility.execute()
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/management/__init__.py", line 356, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/management/base.py", line 283, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/management/base.py", line 327, in execute
    self.check()
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/management/base.py", line 359, in check
    include_deployment_checks=include_deployment_checks,
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/management/base.py", line 346, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/checks/urls.py", line 16, in check_url_config
    return check_resolver(resolver)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/core/checks/urls.py", line 26, in check_resolver
    return check_method()
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/urls/resolvers.py", line 254, in check
    for pattern in self.url_patterns:
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/urls/resolvers.py", line 405, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/urls/resolvers.py", line 398, in urlconf_module
    return import_module(self.urlconf_name)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/theophile/Sites/bugpolyview/bugpolyview/urls.py", line 7, in <module>
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/Users/theophile/Sites/bugpolyview/testappli/urls.py", line 3, in <module>
    from . import views
  File "/Users/theophile/Sites/bugpolyview/testappli/views.py", line 16, in <module>
    class ChildViewSet(viewsets.ModelViewSet):
  File "/Users/theophile/Sites/bugpolyview/testappli/views.py", line 17, in ChildViewSet
    queryset = Child.objects.all()
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/manager.py", line 160, in all
    return self.get_queryset()
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/managers.py", line 37, in get_queryset
    qs = qs.instance_of(self.model)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/query.py", line 146, in instance_of
    return self.filter(instance_of=args)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/query.py", line 784, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/query.py", line 156, in _filter_or_exclude
    additional_args = translate_polymorphic_filter_definitions_in_kwargs(self.model, kwargs, using=self.db)  # filter_field='data'
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/query_translate.py", line 43, in translate_polymorphic_filter_definitions_in_kwargs
    new_expr = _translate_polymorphic_filter_definition(queryset_model, field_path, val, using=using)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/query_translate.py", line 108, in _translate_polymorphic_filter_definition
    return _create_model_filter_Q(field_val, using=using)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/query_translate.py", line 247, in _create_model_filter_Q
    qlist = [q_class_with_subclasses(m) for m in modellist]
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/query_translate.py", line 247, in <listcomp>
    qlist = [q_class_with_subclasses(m) for m in modellist]
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/polymorphic/query_translate.py", line 242, in q_class_with_subclasses
    q = models.Q(polymorphic_ctype=ContentType.objects.db_manager(using).get_for_model(model, for_concrete_model=False))
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/contrib/contenttypes/models.py", line 54, in get_for_model
    ct = self.get(app_label=opts.app_label, model=opts.model_name)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/query.py", line 374, in get
    num = len(clone)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/query.py", line 232, in __len__
    self._fetch_all()
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/query.py", line 1118, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/query.py", line 53, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 899, in execute_sql
    raise original_exception
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 889, in execute_sql
    cursor.execute(sql, params)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/backends/utils.py", line 79, in execute
    return super(CursorDebugWrapper, self).execute(sql, params)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/utils.py", line 94, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/utils/six.py", line 685, in reraise
    raise value.with_traceback(tb)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/Users/theophile/Sites/bugpolyview/venv/lib/python3.6/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: no such table: django_content_type
```
