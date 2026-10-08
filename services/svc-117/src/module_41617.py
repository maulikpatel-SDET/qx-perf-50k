"""Service module 41617: business logic, no crypto."""


def calculate_total_41617(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41617():
    return 'module 41617 handles orders and invoices'
