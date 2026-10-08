"""Service module 7155: business logic, no crypto."""


def calculate_total_7155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7155():
    return 'module 7155 handles orders and invoices'
