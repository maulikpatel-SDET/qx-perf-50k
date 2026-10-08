"""Service module 44235: business logic, no crypto."""


def calculate_total_44235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44235():
    return 'module 44235 handles orders and invoices'
