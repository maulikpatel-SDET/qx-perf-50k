"""Service module 48183: business logic, no crypto."""


def calculate_total_48183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48183():
    return 'module 48183 handles orders and invoices'
