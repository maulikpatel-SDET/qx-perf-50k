"""Service module 49334: business logic, no crypto."""


def calculate_total_49334(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49334():
    return 'module 49334 handles orders and invoices'
