"""Service module 47726: business logic, no crypto."""


def calculate_total_47726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47726():
    return 'module 47726 handles orders and invoices'
