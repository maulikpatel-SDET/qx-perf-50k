"""Service module 47772: business logic, no crypto."""


def calculate_total_47772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47772():
    return 'module 47772 handles orders and invoices'
