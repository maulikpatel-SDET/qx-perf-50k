"""Service module 35772: business logic, no crypto."""


def calculate_total_35772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35772():
    return 'module 35772 handles orders and invoices'
