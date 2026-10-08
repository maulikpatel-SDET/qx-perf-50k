"""Service module 49183: business logic, no crypto."""


def calculate_total_49183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49183():
    return 'module 49183 handles orders and invoices'
