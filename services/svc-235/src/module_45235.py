"""Service module 45235: business logic, no crypto."""


def calculate_total_45235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45235():
    return 'module 45235 handles orders and invoices'
