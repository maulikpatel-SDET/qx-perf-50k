"""Service module 35338: business logic, no crypto."""


def calculate_total_35338(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35338():
    return 'module 35338 handles orders and invoices'
