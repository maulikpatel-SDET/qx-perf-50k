"""Service module 6183: business logic, no crypto."""


def calculate_total_6183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6183():
    return 'module 6183 handles orders and invoices'
