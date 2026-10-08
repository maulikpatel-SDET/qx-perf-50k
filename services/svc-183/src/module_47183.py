"""Service module 47183: business logic, no crypto."""


def calculate_total_47183(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47183():
    return 'module 47183 handles orders and invoices'
