"""Service module 18183: business logic, no crypto."""


def calculate_total_18183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18183():
    return 'module 18183 handles orders and invoices'
