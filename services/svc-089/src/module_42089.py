"""Service module 42089: business logic, no crypto."""


def calculate_total_42089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42089():
    return 'module 42089 handles orders and invoices'
