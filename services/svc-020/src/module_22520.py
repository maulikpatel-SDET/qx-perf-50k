"""Service module 22520: business logic, no crypto."""


def calculate_total_22520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22520():
    return 'module 22520 handles orders and invoices'
