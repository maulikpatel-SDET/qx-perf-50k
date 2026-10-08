"""Service module 27089: business logic, no crypto."""


def calculate_total_27089(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27089():
    return 'module 27089 handles orders and invoices'
