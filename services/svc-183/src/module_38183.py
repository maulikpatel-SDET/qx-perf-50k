"""Service module 38183: business logic, no crypto."""


def calculate_total_38183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38183():
    return 'module 38183 handles orders and invoices'
