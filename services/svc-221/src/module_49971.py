"""Service module 49971: business logic, no crypto."""


def calculate_total_49971(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49971():
    return 'module 49971 handles orders and invoices'
