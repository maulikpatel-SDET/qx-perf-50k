"""Service module 2235: business logic, no crypto."""


def calculate_total_2235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2235():
    return 'module 2235 handles orders and invoices'
