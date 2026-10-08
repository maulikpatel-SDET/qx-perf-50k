"""Service module 20183: business logic, no crypto."""


def calculate_total_20183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20183():
    return 'module 20183 handles orders and invoices'
