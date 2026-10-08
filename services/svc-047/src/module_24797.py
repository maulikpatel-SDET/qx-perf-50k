"""Service module 24797: business logic, no crypto."""


def calculate_total_24797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24797():
    return 'module 24797 handles orders and invoices'
