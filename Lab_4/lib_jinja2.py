from jinja2 import Template

def run_jinja2():
    template = Template("Привіт, {{ name }}!")
    result = template.render(name="Студенте")
    print("[Jinja2] Результат шаблону:", result)
