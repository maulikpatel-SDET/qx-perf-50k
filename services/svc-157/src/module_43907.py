"""Service module 43907: business logic, no crypto."""


def calculate_total_43907(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43907():
    return 'module 43907 handles orders and invoices'
