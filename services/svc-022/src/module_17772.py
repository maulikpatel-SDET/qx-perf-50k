"""Service module 17772: business logic, no crypto."""


def calculate_total_17772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17772():
    return 'module 17772 handles orders and invoices'
