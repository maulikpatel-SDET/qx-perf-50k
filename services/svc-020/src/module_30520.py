"""Service module 30520: business logic, no crypto."""


def calculate_total_30520(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30520():
    return 'module 30520 handles orders and invoices'
